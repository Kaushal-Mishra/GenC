

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCGwtv94hX3XGsTzJ57h3zU_zLE-0M4Vgk"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_c_code(task_description):
    template = f"""
        {task_description}

        Write C code to achieve the task described above.
    """
    response = model.generate_content(template)
    C_code = response.text
    C_code = C_code.replace("```c", "").rstrip("```")
    return C_code

def main():
    st.set_page_config(page_title="C Program Generator", page_icon="🚀")
    st.markdown(
        """
            <div style="text-align:center;">
                <h1>C Program Generator</h1>
                <h3>I can generate C codes for you!</h3>
            </div>
        """,
        unsafe_allow_html=True,
    )

    task_description = st.text_area("Describe the Program:")

    submit = st.button("Generate C Code")

    if submit:
        with st.spinner("Generating C Program Code..."):
            C_code = generate_c_code(task_description)

            with st.container():
                st.success("C Code Generated! Here is your code:")
                st.code(C_code, language="C")

if __name__ == "__main__":
    main()