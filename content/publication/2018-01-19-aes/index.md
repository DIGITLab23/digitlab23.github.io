---
title: "Active Expansion Sampling for Learning Feasible Domains in an Unbounded Input Space"
authors:
- Wei_Chen
- Mark Fuge
date: "2018-01-19"
doi: "10.1007/s00158-017-1894-y"

# Schedule page publish date (NOT publication's date).
publishDate: "2018-01-19"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Structural and Multidisciplinary Optimization, 57*(3)"
publication_short: ""

abstract: Many engineering problems require identifying feasible domains under implicit constraints. One example is finding acceptable car body styling designs based on constraints like aesthetics and functionality. Current active-learning based methods learn feasible domains for bounded input spaces. However, we usually lack prior knowledge about how to set those input variable bounds. Bounds that are too small will fail to cover all feasible domains; while bounds that are too large will waste query budget. To avoid this problem, we introduce Active Expansion Sampling (AES), a method that identifies (possibly disconnected) feasible domains over an unbounded input space. AES progressively expands our knowledge of the input space, and uses successive exploitation and exploration stages to switch between learning the decision boundary and searching for new feasible domains. We show that AES has a misclassification loss guarantee within the explored region, independent of the number of iterations or labeled samples. Thus it can be used for real-time prediction of samples' feasibility within the explored region. We evaluate AES on three test examples and compare AES with a similar method -- the straddle heuristic -- that operates over fixed input variable bounds.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://link.springer.com/article/10.1007/s00158-017-1894-y"
url_pdf: 'https://arxiv.org/pdf/1708.07888'
url_code: 'https://github.com/IDEALLab/Active-Expansion-Sampling'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
