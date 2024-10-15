---
title: "Synthesizing Designs with Inter-part Dependencies Using Hierarchical Generative Adversarial Networks"
authors:
- Wei_Chen
- Mark Fuge
date: "2019-09-16"
doi: "10.1115/1.4044076"

# Schedule page publish date (NOT publication's date).
publishDate: "2019-09-16"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 141*(11)"
publication_short: ""

abstract: Real-world designs usually consist of parts with inter-part dependencies, i.e., the geometry of one part is dependent on one or multiple other parts. We can represent such dependency in a part dependency graph. This paper presents a method for synthesizing these types of hierarchical designs using generative models learned from examples. It decomposes the problem of synthesizing the whole design into synthesizing each part separately but keeping the inter-part dependencies satisfied. Specifically, this method constructs multiple generative models, the interaction of which is based on the part dependency graph. We then use the trained generative models to synthesize or explore each part design separately via a low-dimensional latent representation, conditioned on the corresponding parent part(s). We verify our model on multiple design examples with different inter-part dependencies. We evaluate our model by analyzing the constraint satisfaction performance, the synthesis quality, the latent space quality, and the effects of part dependency depth and branching factor. This paper's techniques for capturing dependencies among parts lay the foundation for learned generative models to extend to more realistic engineering systems where such relationships are widespread.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'files/papers/md_141_11_111403.pdf'
url_code: 'https://github.com/IDEALLab/hgan_jmd_2019'
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
