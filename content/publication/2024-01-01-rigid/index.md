---
title: "Generative Inverse Design of Metamaterials with Functional Responses by Interpretable Learning"
authors:
- Wei_Chen
- Rachel Sun
- Doksoo Lee
- Carlos M. Portela
- Wei Chen
date: "2024-11-07"
doi: "10.1002/aisy.202400611"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-11-07"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Advanced Intelligent Systems*"
publication_short: ""

abstract: Metamaterials with functional responses can exhibit varying properties under different conditions (e.g., wave-based responses or deformation-induced property variation). This work addresses rapid inverse design of such metamaterials to meet target qualitative functional behaviors, a challenge due to its intractability and nonunique solutions. Unlike data-intensive and noninterpretable deep-learning-based methods, this work proposes the random-forest-based interpretable generative inverse design (RIGID), a single-shot inverse design method for fast generation of metamaterials with on-demand functional behaviors. RIGID leverages the interpretability of a random forest-based "design → response" forward model, eliminating the need for a more complex "response → design" inverse model. Based on the likelihood of target satisfaction derived from the trained random forest, one can sample a desired number of design solutions using Markov chain Monte Carlo methods. RIGID is validated on acoustic and optical metamaterial design problems, each with fewer than 250 training samples. Compared to the genetic algorithm-based design generation approach, RIGID generates satisfactory solutions that cover a broader range of the design space, allowing for better consideration of additional figures of merit beyond target satisfaction. This work offers a new perspective on solving on-demand inverse design problems, showcasing the potential for incorporating interpretable machine learning into generative design under small data constraints.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# tags:
# - Source Themes
featured: false

links:
# - name: Link
#   url: https://onlinelibrary.wiley.com/doi/abs/10.1002/aisy.202400611
url_pdf: 'files/papers/2401.00003v5.pdf'
url_code: 'https://github.com/DIGITLab23/RIGID'
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
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

