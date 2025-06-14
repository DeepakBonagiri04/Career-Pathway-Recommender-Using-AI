import gradio as gr
from logic.career_chain import generate_recommendation

def recommend_career(subjects, hobbies, scores):
    try:
        response = generate_recommendation(subjects, hobbies, scores)
        return response
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("""
    # 🎯 Let's find the best career path for you based on your interests, hobbies, and strengths!
    """)

    with gr.Row():
        subjects_input = gr.Textbox(label="📘 Favorite Subjects", placeholder="e.g., Maths, Physics")
        hobbies_input = gr.Textbox(label="🎤 Hobbies / Activities", placeholder="e.g., Cricket, Reading")
        scores_input = gr.Textbox(label="📊 Academic Strengths", placeholder="e.g., 90 in Maths")

    with gr.Row():
        submit_btn = gr.Button("🎯 Recommend Career Path")

    output = gr.Textbox(label="🎯 Recommended Path", lines=15)

    submit_btn.click(
        fn=recommend_career,
        inputs=[subjects_input, hobbies_input, scores_input],
        outputs=output
    )

demo.launch(share=True)
