"""Run the supplied input scenarios against the unchanged assignment programs.

Run from any directory: python verification/run_tests.py
Only standard-library modules are required. FINDING means an observed requirement
or validation gap in the frozen source, not a failed assertion in this runner.
"""
from pathlib import Path
import csv
import hashlib
import json
import platform
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parent / 'python-conditions-loops-assessment'
FILES = {'S':'student_scholarship_system.py','P':'pharmacy_inventory_system.py'}

def main():
    cases = json.loads((HERE / 'test-cases.json').read_text(encoding='utf-8'))
    integrity = json.loads((HERE / 'source-integrity.json').read_text())
    syntax = {}
    for filename in FILES.values():
        data = (REPO / filename).read_bytes()
        assert hashlib.sha256(data).hexdigest() == integrity[filename]['sha256'], f'Source bytes changed: {filename}'
        compile(data, filename, 'exec')
        syntax[filename] = 'PASS'
    results = []
    for case in cases:
        process = subprocess.run([sys.executable,'-B',str(REPO / FILES[case['task']])],input='\n'.join(case['inputs'])+'\n',capture_output=True,text=True,encoding='utf-8',timeout=5)
        errors = []
        for needle in case['observed_contains']:
            if needle not in process.stdout:
                errors.append(f'Missing stdout text: {needle!r}')
        for needle in case['observed_absent']:
            if needle in process.stdout:
                errors.append(f'Unexpected stdout text: {needle!r}')
        if case['error']:
            if process.returncode == 0 or case['error'] not in process.stderr:
                errors.append(f'Expected nonzero exit and {case["error"]}')
        elif process.returncode != 0 or process.stderr:
            errors.append(f'Unexpected error exit {process.returncode}')
        results.append({**case,'exit_code':process.returncode,'stdout':process.stdout,'stderr':process.stderr,'observation_check':'PASS' if not errors else 'FAIL','check_errors':errors})
    summary = {'python':platform.python_version(),'platform':platform.platform(),'scenario_count':len(results),'observation_checks_passed':sum(r['observation_check']=='PASS' for r in results),'requirement_passes':sum(r['requirement_status']=='PASS' for r in results),'requirement_findings':sum(r['requirement_status']=='FINDING' for r in results),'syntax_checks':syntax,'source_integrity':'PASS','tasks':{t:{'scenarios':sum(r['task']==t for r in results),'requirement_passes':sum(r['task']==t and r['requirement_status']=='PASS' for r in results),'findings':sum(r['task']==t and r['requirement_status']=='FINDING' for r in results)} for t in FILES}}
    (HERE / 'test-results.json').write_text(json.dumps({'summary':summary,'results':results},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    with (HERE / 'test-results.csv').open('w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','scenario','inputs','required_result','requirement_status','exit_code','observed_error','observation_check'])
        for r in results:
            writer.writerow([r['id'],r['scenario'],json.dumps(r['inputs'],ensure_ascii=False),r['required_result'],r['requirement_status'],r['exit_code'],r['error'] or '',r['observation_check']])
    print(json.dumps(summary,indent=2))
    if any(r['observation_check']=='FAIL' for r in results):
        print(json.dumps([{'id':r['id'],'errors':r['check_errors']} for r in results if r['check_errors']],indent=2))
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
