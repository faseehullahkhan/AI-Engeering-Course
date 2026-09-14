import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# --------------------------------------------------
# ENVIRONMENT
# --------------------------------------------------

# Loads .env locally.
# On Streamlit Cloud, the API key will come from st.secrets.
load_dotenv()


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Table for One",
    page_icon="🍳",
    layout="wide",
)


# --------------------------------------------------
# STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    :root {
        --bg: #101411;
        --surface: #181e1a;
        --surface-soft: #202821;
        --card: #f2eee4;

        --text-light: #f5f1e8;
        --text-dark: #1b211c;
        --muted-light: #aeb9ae;
        --muted-dark: #6d756d;

        --sage: #9caf88;
        --sage-dark: #748565;
        --cream: #e9dfc8;
        --gold: #d5ad68;

        --border-dark: #2d372f;
        --border-light: #d8d0c1;
    }

    /* --------------------------------------------------
       MAIN APP
    -------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 10%,
                rgba(156, 175, 136, 0.10) 0%,
                transparent 28rem
            ),
            linear-gradient(
                145deg,
                #101411 0%,
                #151b17 55%,
                #0d110e 100%
            );

        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 4rem;
        padding-bottom: 5rem;
    }

    /* --------------------------------------------------
       TYPOGRAPHY
    -------------------------------------------------- */

    h1,
    h2,
    h3 {
        font-family: 'Playfair Display', serif;
    }

    h1 {
        color: var(--text-light);
        font-size: clamp(3rem, 6vw, 6rem);
        line-height: 0.95;
        letter-spacing: -0.035em;
        margin-top: 0.4rem;
        margin-bottom: 1.2rem;
        max-width: 800px;
    }

    .eyebrow {
        display: inline-block;
        color: var(--gold);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        border: 1px solid rgba(213, 173, 104, 0.35);
        border-radius: 999px;
        padding: 0.45rem 0.85rem;
        margin-bottom: 0.7rem;
    }

    .lede {
        color: var(--muted-light);
        font-size: 1.05rem;
        line-height: 1.8;
        max-width: 40rem;
        margin-bottom: 1.8rem;
    }

    /* --------------------------------------------------
       SIDEBAR
    -------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #202821 0%,
                #141a16 100%
            );

        border-right: 1px solid var(--border-dark);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] h2 {
        color: var(--cream);
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] span {
        color: #c4ccc3;
    }

    section[data-testid="stSidebar"] strong {
        color: var(--gold) !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: var(--border-dark);
        margin: 1.5rem 0;
    }

    /* --------------------------------------------------
       FORM CARD
    -------------------------------------------------- */

    div[data-testid="stForm"] {
        background:
            linear-gradient(
                145deg,
                #1c231e 0%,
                #171d19 100%
            );

        border: 1px solid var(--border-dark);
        border-radius: 22px;
        padding: 1.7rem;

        box-shadow:
            0 24px 60px rgba(0, 0, 0, 0.28),
            inset 0 1px 0 rgba(255, 255, 255, 0.025);
    }

    div[data-testid="stForm"] label,
    div[data-testid="stForm"] p {
        color: var(--text-light);
        font-weight: 500;
    }

    /* --------------------------------------------------
       INPUTS
    -------------------------------------------------- */

    .stTextArea textarea {
        background: #111612 !important;
        color: var(--text-light) !important;
        border: 1px solid #303b32 !important;
        border-radius: 12px !important;
        padding: 0.9rem !important;
    }

    .stTextArea textarea::placeholder {
        color: #778278;
    }

    .stTextArea textarea:focus {
        border-color: var(--sage) !important;
        box-shadow:
            0 0 0 2px rgba(156, 175, 136, 0.15) !important;
    }

    .stSelectbox [data-baseweb="select"] > div {
        background: #111612;
        color: var(--text-light);
        border-color: #303b32;
        border-radius: 10px;
    }

    .stSelectbox [data-baseweb="select"] span {
        color: var(--text-light);
    }

    /* --------------------------------------------------
       BUTTON
    -------------------------------------------------- */

    .stButton > button,
    .stFormSubmitButton > button {
        background:
            linear-gradient(
                135deg,
                var(--sage) 0%,
                #b4c79e 100%
            );

        color: #172015;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        font-size: 0.98rem;
        min-height: 3.1rem;

        box-shadow:
            0 8px 24px rgba(156, 175, 136, 0.15);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease,
            background 0.18s ease;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background:
            linear-gradient(
                135deg,
                #b5c9a1 0%,
                #c7d7b7 100%
            );

        color: #111711;
        transform: translateY(-2px);

        box-shadow:
            0 12px 30px rgba(156, 175, 136, 0.23);
    }

    .stButton > button:active,
    .stFormSubmitButton > button:active {
        transform: translateY(0);
    }

    /* --------------------------------------------------
       PLACEHOLDER CARD
    -------------------------------------------------- */

    .recipe-shell {
        position: relative;

        background:
            linear-gradient(
                145deg,
                #f3efe5 0%,
                #ebe4d5 100%
            );

        color: var(--text-dark);
        border: 1px solid var(--border-light);
        border-radius: 24px;
        padding: 2.5rem 2.7rem;

        box-shadow:
            0 25px 70px rgba(0, 0, 0, 0.30);
    }

    .recipe-shell::before {
        content: "";
        position: absolute;
        top: 0;
        left: 2.5rem;
        right: 2.5rem;
        height: 4px;

        background:
            linear-gradient(
                90deg,
                var(--sage-dark),
                var(--gold)
            );

        border-radius: 0 0 10px 10px;
    }

    .recipe-shell h2 {
        color: var(--text-dark);
        font-size: 2rem;
        margin-top: 0.25rem;
    }

    .recipe-shell p {
        color: #394139;
        line-height: 1.75;
    }

    /* --------------------------------------------------
       GENERATED RECIPE
    -------------------------------------------------- */

    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3 {
        color: var(--text-light);
    }

    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li {
        line-height: 1.7;
    }

    div[data-testid="stMarkdownContainer"] strong {
        color: var(--sage);
    }

    /* --------------------------------------------------
       ALERTS
    -------------------------------------------------- */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* --------------------------------------------------
       RESPONSIVE
    -------------------------------------------------- */

    @media (max-width: 900px) {
        .block-container {
            padding-top: 2rem;
        }

        h1 {
            font-size: 3.4rem;
        }

        .recipe-shell {
            padding: 1.8rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# API KEY
# --------------------------------------------------

def get_api_key():
    """
    Local:
        Reads GOOGLE_API_KEY from .env

    Streamlit Cloud:
        Reads GOOGLE_API_KEY from Streamlit Secrets
    """

    # First try local environment variable
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key:
        return api_key

    # Then try Streamlit Cloud secrets
    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")

        if api_key:
            return api_key

    except Exception:
        pass

    return None


# --------------------------------------------------
# GEMINI CLIENT
# --------------------------------------------------

@st.cache_resource
def get_client():
    api_key = get_api_key()

    if not api_key:
        return None

    return genai.Client(api_key=api_key)


# --------------------------------------------------
# RECIPE GENERATION
# --------------------------------------------------

def generate_recipe(
    ingredients: list[str],
    cuisine: str,
    diet: str,
    servings: int,
    time_limit: str,
    mood: str,
) -> str:

    client = get_client()

    if client is None:
        raise ValueError("Google API key is not configured.")

    prompt = f"""
Create one genuinely cookable recipe using these ingredients: {', '.join(ingredients)}.

Requirements:
- Cuisine direction: {cuisine}
- Dietary preference: {diet}
- Servings: {servings}
- Maximum cooking time: {time_limit}
- Desired mood: {mood}
- Use common pantry staples when helpful, but call them out clearly.
- Never invent an ingredient that conflicts with the dietary preference.
- Make reasonable substitutions if an ingredient is unusual or missing.

Format the answer in Markdown with exactly these sections:

1. A memorable recipe title and one-sentence description.
2. **Ingredients** with quantities.
3. **Method** as numbered, practical steps.
4. **Make it better** with two useful tips and one substitution.
5. A final line with prep time, cook time, and servings.

Keep the recipe under 450 words.
Be specific and appetizing, not generic.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## Recipe studio")

    st.caption(
        "Tell us what is in the kitchen. "
        "We will handle the rest."
    )

    st.divider()

    st.markdown("**Good prompts start with:**")

    st.markdown(
        "- Ingredients you need to use\n"
        "- A cuisine you are craving\n"
        "- Your time and dietary limits"
    )


# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    '<p class="eyebrow">Your next good meal</p>',
    unsafe_allow_html=True,
)

st.title(
    "A better recipe\n"
    "from what you have."
)

st.markdown(
    """
    <p class="lede">
        Turn a handful of ingredients into a thoughtful recipe
        with clear quantities, unfussy steps, and a little
        culinary imagination.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")


# --------------------------------------------------
# LAYOUT
# --------------------------------------------------

left, right = st.columns(
    [0.95, 1.25],
    gap="large",
)


# --------------------------------------------------
# FORM
# --------------------------------------------------

with left:

    with st.form("recipe_form"):

        ingredients_text = st.text_area(
            "What ingredients should we use?",
            placeholder=(
                "potatoes, chickpeas, spinach, "
                "lemon, garlic"
            ),
            height=130,
        )

        cuisine = st.selectbox(
            "Cuisine direction",
            [
                "Any",
                "Pakistani",
                "Mediterranean",
                "Italian",
                "Mexican",
                "Indian",
                "East Asian",
            ],
        )

        diet = st.selectbox(
            "Dietary preference",
            [
                "Any",
                "Vegetarian",
                "Vegan",
                "Halal",
                "High-protein",
                "Gluten-free",
            ],
        )

        servings = st.slider(
            "Servings",
            min_value=1,
            max_value=8,
            value=2,
        )

        time_limit = st.select_slider(
            "Time available",
            options=[
                "15 minutes",
                "30 minutes",
                "45 minutes",
                "1 hour",
                "No limit",
            ],
            value="30 minutes",
        )

        mood = st.selectbox(
            "What sounds good?",
            [
                "Comforting",
                "Fresh and bright",
                "Spicy",
                "Crispy",
                "Light",
                "A little fancy",
            ],
        )

        submitted = st.form_submit_button(
            "Create my recipe",
            use_container_width=True,
        )


# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

with right:

    if submitted:

        ingredients = [
            item.strip()
            for item in ingredients_text.split(",")
            if item.strip()
        ]

        if not ingredients:

            st.warning(
                "Add at least one ingredient so the "
                "recipe has somewhere to begin."
            )

        elif not get_api_key():

            st.error(
                "Google API key is not configured."
            )

        else:

            with st.spinner(
                "Thinking through the flavors..."
            ):

                try:

                    recipe = generate_recipe(
                        ingredients=ingredients,
                        cuisine=cuisine,
                        diet=diet,
                        servings=servings,
                        time_limit=time_limit,
                        mood=mood,
                    )

                    # Recipe is displayed directly.
                    # No empty wrapper/card appears after generation.
                    st.markdown(recipe)

                except Exception as error:

                    st.error(
                        "The recipe could not be generated "
                        f"right now: {error}"
                    )

    else:

        st.markdown(
            """
            <div class="recipe-shell">
                <h2>Your recipe will appear here.</h2>
                <p>
                    Choose your ingredients and preferences,
                    then let the kitchen improvise.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )