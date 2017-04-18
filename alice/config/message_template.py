RELEASE_NOTES = "https://docs.google.com/a/moengage.com/spreadsheets/d/1eW3y-GxGzu8Jde8z4EYC6fRh1Ve4TpbW5qv2-iWs1ks/edit?usp=sharing "
MSG_BAD_START = "Very Bad "
MSG_NO_TECH_REVIEW = "{name} :rage: {pr} is merged into `{branch}` without a \"Tech +1\", soon these kind of requests will" \
      " be automatically reverted CC: {team}"
MSG_NO_PRODUCT_REVIEW = "{name} :rage: {pr} is merged into `{branch}` without \"Product +1\", soon these kind of requests will" \
                " be automatically reverted CC: {team}"

MSG_CODE_CHANNEL = "Title=\"{title}\", Description=\"{desc}\" \nPR: {pr}\n from {head_branch} into `{base_branch}`" \
                   " By: *{pr_by}*, mergedBy: {merge_by}\n" #can remove not required data

MSG_RELEASE_PREPARATION = "\n Please review and approve with +1, Release preparation starts..."

MSG_GUIDELINE_ON_MERGE = "Hi @{person}: you have merged {pr_link} into {base_branch}\n now, be nice & mention it " \
                         "in Release Notes for getting it `QAed and released` " \
                         "under Sheet name as respective Date \n " + RELEASE_NOTES

MSG_AUTO_CLOSE = "alice have auto-closed it because she sensed it an accidental PR (only \"{tested_branch}\" " \
                 "can be merged to \"{main_branch}\") \n Alice is smart! Be like Alice!"

general_comment = { "body": "Did you remember to?\n"
            "- [ ] Add Test Case(s) [how to check](https://github.com/moengage/MoEngage/wiki/jenkins#unit-tests)\n"
            "- [ ] P0 Tests Executed EndToEnd? [what is it](https://github.com/moengage/MoEngage/wiki/p0%20list)?\n"
}

special_comment = {
    "body": "**Attention!** \n Release Checklist\n"
            "- [ ] JS version Update? check index.html\n"
            "- [ ] No code/PR to be reverted? check release notes\n"
            "- [ ] Unit Tests Passed?\n"
            "- [ ] Api Tests passed?\n"
            "- [ ] QA report linked?\n"
            "- [ ] Release Notes linked?"
}

