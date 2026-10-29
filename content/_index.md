---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content: 
      text: |
        <div style="padding: 2rem 0;">
          <h1>DIGIT Lab</h1>
          <img src="img/landing_figure.svg" alt="A designer at the center of a design space that AI expands, with trust and discovery flowing back to people" style="float: right; margin: 0 0 10px 20px; width: 600px;">
        
          In the <u>D</u>esign <u>I</u>nnovation & <u>G</u>enerative <u>I</u>n<u>t</u>elligence (DIGIT) Lab, we answer this overarching question: **How can AI augment our ability to design better materials, structures, and engineered systems?** Our work has two sides. First, we leverage AI to push the limits of what can be designed. This involves unlocking design complexity beyond the capability of traditional methods and enabling the discovery of "outside-the-box" solutions. Meanwhile, we keep people at the center of this process by making AI-driven design trustworthy to engineers and turning what AI learns into knowledge that makes us better designers.

          Toward these goals, we develop computational methods for generative design and design under uncertainty, demonstrated on problems ranging from aerodynamic shapes to engineered materials. Learn more about our [**research**](/research/) and [**publications**](/publication/).

        </div>

  - block: markdown
    content:
      title: Join Us!
      subtitle: ''
      text: |
        <br>
        
        Are you passionate about pushing the boundaries of AI and machine learning for engineering design? We have openings for fully funded Ph.D. positions starting **Fall 2027**, and we’re looking for enthusiastic individuals to [**join our team**](/join/)! 

  
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

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the Team" %}}
    design:
      columns: '1'
---