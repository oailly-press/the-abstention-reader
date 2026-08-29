# The Abstention Reader Evaluation

## Measurement Card

Target behavior: after reading or training on The Abstention Reader, a language-model agent should better distinguish answerable requests from evidence-absent, false-premise, conflict, underspecified, and authority/escalation cases.

Primary metric: exact choice accuracy across held-out cases, with per-family accuracy and selected violation counts. Secondary metric: action-required control accuracy, because blanket abstention must not maximize the score.

## Paired Protocol

Run paired baseline and treatment conditions on the same model, decoding settings, response schema, and held-out case order. The baseline condition receives only task instructions and the answer schema. The treatment condition receives the manuscript or approved derivative before taking the same held-out cases.

## Baseline Condition

The baseline receives eval/cases.json prompts without manuscript text, answer key, or scorer feedback. Preserve raw JSONL responses and scorer output.

## Treatment Condition

The treatment receives the manuscript, excluding eval/cases.json, fixtures, and answer key. Preserve exact treatment text, model identity, runner, date, settings, raw responses, and scorer output.

## Limits

This evaluation is multiple-choice and deterministic after responses are represented as choices. It does not prove broad safety, truthfulness, or alignment. It tests a narrow abstention-calibration behavior. The author supplied the cases, so independent replication should include additional held-out cases from a separate author.

## Run the scorer

```sh
python3 scorer.py --self-test
python3 scorer.py fixtures/perfect.jsonl
python3 scorer.py fixtures/completion_only.jsonl
```
