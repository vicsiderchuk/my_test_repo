USER_NAME = "v_siderchuk"

VALID_CREATE_MEME_PAYLOAD = {
    "text": "This is fine",
    "url": "https://static01.nyt.com/images/2016/08/05/us/05onfire1_xp/05onfire1_xp-superJumbo-v2.jpg",
    "tags": ["dog", "fire", "mug"],
    "info": {"color": "orange", "year": 2026, "popularity": "high"}
    }

VALID_UPDATE_MEME_PAYLOAD = {
    "text": "UPD by autotest",
    "url": "https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80",
    "tags": ["dino_UPD", "expectations"],
    "info": {"year": 2021, "popularity": "low", "new_info": "test123!_UPD"}
}

INVALID_MEME_PAYLOAD = [
    # "text" is int instead of str
    {
    "text": 123,
    "url": "https://example.com",
    "tags": ["autotest_tag"],
    "info": {"year": 2021}
    },
    # "url" is boolean instead of str
    {
        "text": "autotest_text",
        "url": True,
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
    # "tags" is str instead of list
    {
        "text": "autotest_text",
        "url": "https://example.com",
        "tags": "string",
        "info": {"year": 2021}
    },
    # "info" is str instead of dict
    {
        "text": "autotest_text",
        "url": "https://example.com",
        "tags": ["autotest_tag"],
        "info": "string"
    },
    # empty body
    {},
    # "text" is missing
    {
        "url": "https://example.com",
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
    # "url" is missing
    {
        "text": "autotest_text",
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
    # "tags" is missing
    {
        "text": "autotest_text",
        "url": "https://example.com",
        "info": {"year": 2021}
    },
    # "info" is missing
    {
        "text": "autotest_text",
        "url": "https://example.com",
        "tags": ["autotest_tag"]
    },
    # "text" is empty str
    {
        "text": "",
        "url": "https://example.com",
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
    # text is None
    {
        "text": None,
        "url": "https://example.com",
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
    # "url" is empty str
    {
        "text": "autotest_text",
        "url": "",
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
    # "url" is None
    {
        "text": "autotest_text",
        "url": None,
        "tags": ["autotest_tag"],
        "info": {"year": 2021}
    },
]

INVALID_AUTH_PAYLOAD = [
    # empty body
    {},
    # "name" is empty str
    {"name": ""},
    # "name" is None
    {"name": None},
    # "name" is int instead of str
    {"name": 12}
]
