from playwright.sync_api import sync_playwright
import json

lessons_id = [33623636, 33623620, 37175860, 33623623, 33623645, 33623617, 33623590, 33623577, 33623648, 33623651, 33623650, 33623605, 33623584, 33623580]
lessons_name = ['biology', 'geography', 'english', 'informatics', 'history', 'literature', 'russian', 'chemistry', 'algebra', 'statistics', 'geometry', 'social-science', 'physics', 'pe']

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    page.route(
        "**/*",
        lambda route, request:
            route.abort()
            if request.resource_type in ["image", "font", "stylesheet"]
            else route.continue_()
    )

    def is_needed(response):
        return (
            "api/ej/rating/v1/rank/class" in response.url
            and response.status == 200
        )

    for i in range(len(lessons_id)):
        print(lessons_name[i])
        with page.expect_response(is_needed) as resp_info:
            page.goto("https://school.mos.ru/diary/marks/current-marks/?view=by_subject&subject_id=" +str(lessons_id[i]))

        response = resp_info.value
        data = response.json()

        with open('mesh-parser/data/data-'+str(lessons_name[i])+'.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print()

    browser.close()
