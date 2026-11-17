# Verification evidence

Both application source files were preserved exactly, including their CRLF line endings. SHA-256 hashes are recorded in `source-integrity.json`.

| Check | Result |
| --- | --- |
| Source-byte identity | Both files match the uploaded originals |
| Syntax compilation | Both compile under Python 3.12.14 |
| Real program executions | 84 scenarios: 40 scholarship, 44 pharmacy |
| Behavior meeting stated expectations | 40 scenarios |
| Requirement or validation findings | 44 scenarios; several reproduce the same underlying defect |
| Recorded observations reproduced | 84 of 84 checks |
| SVG XML and resource checks | All five SVGs are valid XML and use no external resources |
| PNG rendering and bounds | All five rendered; text bounds fit each canvas |
| Diagram appearance | PNG renderings inspected for clipping, overlap and arrowheads |
| README structure and references | Requested section order, 84 test rows and valid relative file links |
| HTML previews | Parsed and self-contained, with all five diagrams embedded |
| Preview controls | JavaScript syntax checked; theme, expand/collapse and source-viewer logic tested in a Node DOM fixture |
| Preview visual browser check | Not performed: local HTML navigation is blocked by the preview browser policy |

The HTML files are rendered from the Markdown and include responsive styles for desktop and mobile. Open them locally to review their final browser appearance. No browser screenshots are included.

## Files

- `run_tests.py`: standard-library runner; checks hashes, compiles the applications in memory and executes every scenario.
- `test-cases.json`: input values, assertions and requirement expectations for all 84 scenarios.
- `test-results.json`: full stdout, stderr, return codes and summary from actual subprocess executions.
- `test-results.csv`: compact spreadsheet-friendly results.
- `source-integrity.json`: original upload filenames, byte counts and SHA-256 hashes.
- `artifact-validation.json`: diagram, README and HTML validation results.
- `S02-terminal.txt`, `S04-terminal.txt`, `S06-terminal.txt`: captured scholarship terminal transcripts.
- `P02-terminal.txt`, `P06-terminal.txt`, `P23-terminal.txt`: captured pharmacy terminal transcripts.
- `package-manifest.json`: SHA-256 hashes for all other files in the complete package.

## Run again

Keep this folder beside `python-conditions-loops-assessment/` and run from the extracted outer directory:

```bash
python verification/run_tests.py
```

Use `python3` or `py` if required by your environment. No third-party packages are needed for this runner. It writes fresh results into this folder. A successful runner exit confirms the recorded behavior, including error cases; it does not claim the applications satisfy every requirement.
