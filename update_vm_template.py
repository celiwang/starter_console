from pathlib import Path

html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Oracle Cloud Infrastructure Console — Virtual Machine Detail</title>
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
  <link href=\"https://fonts.googleapis.com/css2?family=Red+Hat+Text:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">
  <link rel=\"stylesheet\" href=\"styles.css\" />
</head>
<body>
  <header class=\"console-branding-bar search-v2\">
"""  # truncated for brevity

Path('vm-template.html').write_text(html)
