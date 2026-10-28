---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content: 
      text: |
        <div class="intro">
        <div class="intro-text">
        <h1>DIGIT Lab</h1>
        <p>In the <u>D</u>esign <u>I</u>nnovation &amp; <u>G</u>enerative <u>I</u>n<u>t</u>elligence (DIGIT) Lab, we study <strong>how AI can design better materials, structures, and machines</strong>. Our research focus extends beyond model performance and efficiency, exploring how AI can fundamentally advance design across four key dimensions:</p>
        <ol class="pillar-list">
        <li><strong>Complexity:</strong> How can AI unlock design complexities that are fundamentally inaccessible to traditional methods?</li>
        <li><strong>Trustworthiness:</strong> How can we develop AI-driven design methodologies that engineers can trust?</li>
        <li><strong>Discoverability:</strong> How can AI discover new knowledge that expands human understanding and guides design innovation?</li>
        <li><strong>Creativity:</strong> How can AI enable or accelerate the discovery of "out-of-the-box" design solutions and become a true inventor?</li>
        </ol>
        <p>Guided by these fundamental questions, we develop computational methodologies for design ideation, generative design, and design for X ("X" can represent manufacturing, sustainability, reliability, and beyond) across diverse engineering domains.</p>
        </div>
        <div class="intro-figure">
        <img src="img/landing_page_image.png" alt="DIGIT Lab Research">
        </div>
        </div>

#  - block: markdown
#    content:
#      title: Join Us!
#      subtitle: ''
#      text: |
#        <br>
#        
#        Are you passionate about pushing the boundaries of AI and machine learning for engineering design? At the DIGIT Lab, we are committed to research in this exciting field---and you can be part of it! We have openings for **fully-funded Ph.D. positions** starting Fall 2025, and we’re looking for enthusiastic individuals to join our team! 
#        
#        [Learn More >](/join/)

  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: news
    design:
      view: compact
      columns: '1'
      css_class: news-list

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
