"""Scan for remaining real Chinese text (not just punctuation) in frontend."""
import re, glob

# Only match actual Chinese characters, not punctuation
chinese_char = re.compile(r'[\u4e00-\u9fff]')

results = {}
for f in sorted(glob.glob("frontend/src/**/*.vue", recursive=True) + glob.glob("frontend/src/**/*.js", recursive=True)):
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            for i, line in enumerate(fh, 1):
                if chinese_char.search(line):
                    s = line.strip()
                    # Extract only Chinese character sequences
                    chars = re.findall(r'[\u4e00-\u9fff]+', line)
                    if chars:
                        key = f.replace('\\', '/')
                        if key not in results:
                            results[key] = []
                        # Classify
                        is_comment = s.startswith('//') or s.startswith('/*') or s.startswith('*') or s.startswith('<!--')
                        if not is_comment and '//' in s:
                            before = s[:s.index('//')]
                            if not chinese_char.search(before):
                                is_comment = True
                        tag = "COMMENT" if is_comment else "TEXT"
                        results[key].append((i, tag, ' '.join(chars), s[:120]))
    except:
        pass

total_text = 0
total_comment = 0
for f, items in results.items():
    texts = [x for x in items if x[1] == "TEXT"]
    comments = [x for x in items if x[1] == "COMMENT"]
    if texts:
        print(f"\n{'='*60}")
        print(f"FILE: {f} ({len(texts)} text, {len(comments)} comments)")
        print(f"{'='*60}")
        for line_num, tag, chars, context in texts:
            print(f"  L{line_num}: {chars}")
            print(f"    > {context}")
        total_text += len(texts)
    total_comment += len(comments)

print(f"\n\nSUMMARY: {total_text} visible text lines, {total_comment} comment-only lines")
