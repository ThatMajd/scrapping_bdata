from selenium.webdriver.common.by import By

BUTTONS = {
    "SHOW_MORE": [By.CLASS_NAME, """""show-more-less-html__button show-more-less-button
        show-more-less-html__button--more
        ml-0.5"""],
    "JOB_PAGE": [By.CSS_SELECTOR, "body > div.base-serp-page > div > section"],
    "DESCRIPTION": [By.CSS_SELECTOR, "body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > div > section > div"],
    "COMPANY_ID": [By.CSS_SELECTOR, "body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > section > div > div.top-card-layout__entity-info-container.flex.flex-wrap.papabear\:flex-nowrap > div > h4 > div.face-pile.flex.see-who-was-hired > a"],
    "TOP_BAR": [By.CSS_SELECTOR, "body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > section > div"],
    "BOTTOM_BAR": [By.CSS_SELECTOR, "body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > ul"],
    "LOAD_MORE": [By.CSS_SELECTOR, "#main-content > section > button"]
}

COLS = ['company_id', 'description', 'formatted_experience_level', 'formatted_work_type', 'industries', 'job_function', 'job_id', 'location', 'title', 'work_type']