---
title: "t-METASET: Tailoring Property Bias of Large-Scale Metamaterial Datasets through Active Learning"
authors:
- Doksoo Lee
- Yu-Chin Chan
- Wei_Chen
- Liwei Wang
- Anton van Beek
- Wei Chen
date: "2022-09-11"
doi: "10.1115/1.4055925"

# Schedule page publish date (NOT publication's date).
publishDate: "2022-09-11"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 145*(3)"
publication_short: ""

abstract: Inspired by the recent achievements of machine learning in diverse domains, data-driven metamaterials design has emerged as a compelling paradigm that can unlock the potential of multiscale architectures. The model-centric research trend, however, lacks principled frameworks dedicated to data acquisition, whose quality propagates into the downstream tasks. Often built by naive space-filling design in shape descriptor space, metamaterial datasets suffer from property distributions that are either highly imbalanced or at odds with design tasks of interest. To this end, we present t-METASET&#58; an active learning-based data acquisition framework aiming to guide both diverse and task-aware data generation. Distinctly, we seek a solution to a commonplace yet frequently overlooked scenario at early stages of data-driven design of metamaterials&#58; when a massive (∼O(104)) shape-only library has been prepared with no properties evaluated. The key idea is to harness a data-driven shape descriptor learned from generative models, fit a sparse regressor as a start-up agent, and leverage metrics related to diversity to drive data acquisition to areas that help designers fulfill design goals. We validate the proposed framework in three deployment cases, which encompass general use, task-specific use, and tailorable use. Two large-scale mechanical metamaterial datasets are used to demonstrate the efficacy. Applicable to general image-based design representations, t-METASET could boost future advancements in data-driven design.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'files/papers/2202.10565.pdf'
url_code: ''
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
