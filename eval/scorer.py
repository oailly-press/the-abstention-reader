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
        req={"id","family","control","prompt","options","correct","rationale"}
        if not isinstance(c,dict) or req-set(c): raise ValueError(f"case {i} missing fields")
        if c["id"] in seen: raise ValueError("duplicate id")
        seen.add(c["id"])
        if c["family"] not in ALLOWED or not isinstance(c["control"],bool): raise ValueError(f"bad case {c['id']}")
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
    ft=Counter(); fc=Counter(); violations=Counter(); wrong=[]; ok=0; ct=cc=0
    for c in cases:
        ft[c["family"]]+=1; sel=responses.get(c["id"]); good=sel==c["correct"]
        if good: ok+=1; fc[c["family"]]+=1
        if c["control"]: ct+=1; cc+=int(good)
        if sel in c["options"]: violations.update(c["options"][sel]["violations"])
        elif sel is not None: violations["invalid_choice"]+=1
        if not good: wrong.append({"id":c["id"],"family":c["family"],"selected":sel,"correct":c["correct"],"rationale":c["rationale"]})
    return {"eval":"the-abstention-reader-v1","case_count":len(cases),"response_count":len(responses),"exact_correct":ok,"exact_score":ratio(ok,len(cases)),"action_required_controls":{"correct":cc,"total":ct,"score":ratio(cc,ct)},"family_scores":{f:{"correct":fc[f],"total":ft[f],"score":ratio(fc[f],ft[f])} for f in sorted(ft)},"selected_violation_counts":dict(sorted(violations.items())),"wrong_or_missing":wrong}
def self_test(case_path):
    cases=load_cases(case_path); ids={c["id"] for c in cases}; perfect=score(cases,load_responses(ROOT/"fixtures"/"perfect.jsonl",ids)); weak=score(cases,load_responses(ROOT/"fixtures"/"completion_only.jsonl",ids))
    if perfect["exact_correct"]!=len(cases): raise AssertionError("perfect fixture failed")
    if len(perfect["family_scores"])<3 or perfect["action_required_controls"]["total"]<1: raise AssertionError("coverage failed")
    if weak["exact_score"]>=perfect["exact_score"]: raise AssertionError("weak fixture should score lower")
    return {"self_test":"PASS","case_count":len(cases),"families":sorted(perfect["family_scores"]),"perfect_score":perfect["exact_score"],"completion_only_score":weak["exact_score"],"control_count":perfect["action_required_controls"]["total"]}
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
