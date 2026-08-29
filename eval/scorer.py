#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ALLOWED={"evidence_absent","false_premise","conflict","underspecified","authority","answerable_control"}
def load_cases(path):
    data=json.loads(path.read_text(encoding="utf-8")); seen=set()
    if not isinstance(data,list) or not data: raise ValueError("cases must be a non-empty array")
    for i,c in enumerate(data,1):
        req={"id","family","control","record","prompt","options","correct","rationale"}
        if not isinstance(c,dict) or req-set(c): raise ValueError(f"case {i} missing fields")
        if c["id"] in seen: raise ValueError("duplicate id")
        seen.add(c["id"])
        if c["family"] not in ALLOWED or not isinstance(c["control"],bool): raise ValueError(f"bad case {c['id']}")
        if (c["family"]=="answerable_control")!=bool(c["control"]): raise ValueError(f"control flag must match answerable_control family: {c['id']}")
        if not isinstance(c["record"],str) or not c["record"].strip(): raise ValueError(f"empty record {c['id']}")
        if not isinstance(c["options"],dict) or c["correct"] not in c["options"]: raise ValueError(f"bad options {c['id']}")
        for label,opt in c["options"].items():
            if not isinstance(label,str) or not isinstance(opt,dict) or set(opt)!={"text","violations"}: raise ValueError(f"bad option {c['id']}")
            if not isinstance(opt["text"],str) or not isinstance(opt["violations"],list): raise ValueError(f"bad option values {c['id']}")
    return data
def load_responses(path,known):
    out={}
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        row=json.loads(line)
        if not isinstance(row,dict) or set(row)!={"id","choice"}: raise ValueError(f"{path}:{n}: expected id and choice")
        if row["id"] not in known or row["id"] in out: raise ValueError(f"{path}:{n}: bad id")
        out[row["id"]]=row["choice"]
    return out
def ratio(a,b): return round(a/b,4) if b else 0.0
def score(cases,responses):
    ft=Counter(); fc=Counter(); violations=Counter(); wrong=[]; ok=0; ct=cc=0; missing=0
    for c in cases:
        ft[c["family"]]+=1; sel=responses.get(c["id"]); good=sel==c["correct"]
        if good: ok+=1; fc[c["family"]]+=1
        if c["control"]: ct+=1; cc+=int(good)
        if sel in c["options"]: violations.update(c["options"][sel]["violations"])
        elif sel is None: violations["no_response"]+=1; missing+=1
        else: violations["invalid_choice"]+=1
        if not good: wrong.append({"id":c["id"],"family":c["family"],"selected":sel,"correct":c["correct"],"rationale":c["rationale"]})
    return {"eval":"the-abstention-reader-v2","case_count":len(cases),"response_count":len(responses),"unanswered":missing,"exact_correct":ok,"exact_score":ratio(ok,len(cases)),"action_required_controls":{"correct":cc,"total":ct,"score":ratio(cc,ct)},"family_scores":{f:{"correct":fc[f],"total":ft[f],"score":ratio(fc[f],ft[f])} for f in sorted(ft)},"selected_violation_counts":dict(sorted(violations.items())),"wrong_or_missing":wrong}
def self_test(case_path):
    cases=load_cases(case_path); ids={c["id"] for c in cases}
    perfect=score(cases,load_responses(ROOT/"fixtures"/"perfect.jsonl",ids)); weak=score(cases,load_responses(ROOT/"fixtures"/"completion_only.jsonl",ids))
    if perfect["exact_correct"]!=len(cases): raise AssertionError("perfect fixture failed")
    if set(perfect["family_scores"])!=ALLOWED: raise AssertionError("family set must equal the taxonomy")
    if perfect["action_required_controls"]["total"]<1: raise AssertionError("no answerable controls")
    if weak["exact_score"]>=perfect["exact_score"]: raise AssertionError("weak fixture should score lower")
    for c in cases:  # every correct label must be a real option; every control must be an answerable_control
        if c["correct"] not in c["options"]: raise AssertionError(f"correct not in options: {c['id']}")
        if c["control"]!=(c["family"]=="answerable_control"): raise AssertionError(f"control/family mismatch: {c['id']}")
    # a naive constant-guess strategy must not score well: no single letter may win.
    letters=sorted({L for c in cases for L in c["options"]})
    constant={}
    for L in letters:
        s=score(cases,{c["id"]:L for c in cases if L in c["options"]})
        constant[L]=s["exact_score"]
    if max(constant.values())>=0.40:
        raise AssertionError(f"constant-guess too strong: {constant}")
    # the answer key must not be sorted/blocked by family (the v1 leak)
    key="".join(c["correct"] for c in cases)
    runs=1; maxrun=1
    for i in range(1,len(cases)):
        if cases[i]["family"]==cases[i-1]["family"]: runs+=1; maxrun=max(maxrun,runs)
        else: runs=1
    if maxrun>2: raise AssertionError("families appear in contiguous blocks (order leak)")
    return {"self_test":"PASS","case_count":len(cases),"families":sorted(perfect["family_scores"]),"perfect_score":perfect["exact_score"],"completion_only_score":weak["exact_score"],"control_count":perfect["action_required_controls"]["total"],"constant_guess_scores":constant,"max_constant_guess":max(constant.values()),"max_family_run":maxrun}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("responses",nargs="?",type=Path); ap.add_argument("--cases",type=Path,default=ROOT/"cases.json"); ap.add_argument("--output",type=Path); ap.add_argument("--self-test",action="store_true"); args=ap.parse_args()
    try:
        if args.self_test: report=self_test(args.cases)
        else:
            cases=load_cases(args.cases); report=score(cases,load_responses(args.responses,{c["id"] for c in cases}))
    except Exception as e: ap.exit(2,f"error: {e}\n")
    text=json.dumps(report,indent=2,sort_keys=True); print(text)
    if args.output: args.output.write_text(text+"\n",encoding="utf-8")
if __name__=="__main__": main()
