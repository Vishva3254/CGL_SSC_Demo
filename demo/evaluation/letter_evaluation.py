from groq import Groq
import re
import json

def clean_invalid_chars(text):
    return re.sub(r'[\x00-\x1F\x7F]', '', text)

def safe_json_parse(text):
    try:
        return json.loads(text), None
    except json.JSONDecodeError as e:
        return None, str(e)

def evaluate_ssc_letter(question, letter_text, difficulty_type="easy"):
    
    client = Groq(api_key="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")  
    
    marking_scheme = {
        "Relevance": 10,
        "Spelling_Grammar": 5,
        "Word_Limit": 5,
        "Content_Quality": 8,
        "Format": 5,
        "Writing_Neatness": 5,
        "Effective_Sentences": 7,
        "Cohesiveness": 5
    }
    
    # prompt = f"""
    # Assume you are an examiner for the SSC CGL descriptive writing test. Your task is to evaluate the response solely based on the given prompt for the following criteria: Lexical Resource, Grammatical Range and Accuracy, Task Achievement, and Coherence and Cohesion. Assign marks from 0-50 for each criterion based on the provided description. Remain consistent in your assessment even if the same response is submitted multiple times.
    # Evaluate based on the selected difficulty level: {difficulty_type}.

    # 1. **Lexical Resource**: The range and accuracy of vocabulary used in the letter.
    # 2. **Grammatical Range and Accuracy**: The complexity and correctness of the grammar used.
    # 3. **Task Achievement**: How well the letter addresses the question, providing relevant arguments and supporting details.
    # 4. **Coherence and Cohesion**: The flow and organization of ideas and the use of transitions between sentences and paragraphs.

    # The letter/application is expected to follow the structure of:
    # - **Sender's Address**: Include all necessary contact details (email, residential address, etc.).
    # - **Date**: The date the letter is written.
    # - **Designation and Address of the Addressee**: Whom the letter is being addressed to.
    # - **Subject**: Clearly state the purpose of the letter.
    # - **Salutation**: Use a formal greeting (e.g., Respected Sir/Ma’am).
    # - **Introduction**: Briefly state the purpose of writing the letter and the issue at hand.
    # - **Body**: Elucidate the details of the issue in clear, concise sentences.
    # - **Conclusion**: Reiterate the purpose of writing the letter, thank the reviewer, and provide a closing salutation.
    # - **Sender’s Name and Designation**: End the letter with the sender’s name and position.

    # The SSC CGL letter is evaluated on the following marking scheme {marking_scheme} with description:
    # - **Relevance**: How well the letter addresses the topic (10 marks).
    # - **Spelling/Grammar**: Accuracy in spelling and grammar (5 marks).
    # - **Word Limit**: Adherence to the word limit in 150-175 words (5 marks). 
    # - **Content Quality**: Depth and clarity of content (8 marks).
    # - **Format**: Proper letter format (5 marks).
    # - **Writing Neatness**: Clarity and neatness of writing (5 marks).
    # - **Effective Sentences**: Use of varied and clear sentence structures (7 marks).
    # - **Cohesiveness**: Logical flow and transitions between ideas (5 marks).

    # Please evaluate the letter based on these criteria. Provide scores for each category, explain why the scores were assigned, and suggest improvements. Also, give an example of a perfect 50-mark answer for the question.'And also the total marks given should be out of 50'.
    # Remember if there is nothing like the answer is blank then all score will be 0 and also remember this strictly that if the answer is not based on the question or is in other direction then also all the scores will be 0. (please evaluate this very strictly)
    
    # Application Question: "{question}"
    # Letter Text: "{letter_text}"

    # *Final Output (Strictly in JSON format with no extra text or comments)*:
    # {{
    #     "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation_for_relevance_score}}"],
    #     "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation_for_spelling_grammar_score}}"],
    #     "Word_Limit_Marks":[{{Word_Limit_Marks}}, "{{Explanation_for_word_limit_score}}"],
    #     "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation_for_content_quality_score}}"],
    #     "Format_Marks": [{{Format_Marks}}, "{{Explanation_for_format_score}}"],
    #     "Writing_Neatness_Marks":[{{Writing_Neatness_Marks}}, "{{Explanation_for_writing_neatness_score}}"],
    #     "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation_for_effective_sentences_score}}"],
    #     "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation_for_cohesiveness_score}}"],
    #     "Total_Marks": [{{Total_Marks}}, "{{Explanation_for_Total_Marks}}"],
    #     "Strengths": "[List of strengths from the user's answer]",
    #     "Weaknesses": "[List of weaknesses from the user's answer that need improvement]",
    #     "50_Marks_Answer": "[Generate a 50-mark answer for the letter writing question of SSC CGL descriptive part, ensuring it addresses all marking criteria comprehensively, with '100-150 words' in response to {question}]",
    #     "AI_Suggestions": "[Provide specific suggestions for improvement based on the user's answer in {letter_text}]",
    #     "Improved_Solution": "[Provide a 50-mark improved solution for the user's answer {letter_text} based on the application question asked which was {question}]"
    # }}
    # """
    # prompt = f"""
    # Assume you are an examiner for the SSC CGL descriptive writing test. Your task is to evaluate the response solely based on the given prompt for the following criteria: Lexical Resource, Grammatical Range and Accuracy, Task Achievement, and Coherence and Cohesion. Assign marks from 0-50 for each criterion based on the provided description. Remain consistent in your assessment even if the same response is submitted multiple times.
    # Evaluate based on the selected difficulty level: {difficulty_type}.

    # 1. **Lexical Resource**: The range and accuracy of vocabulary used in the letter.
    # 2. **Grammatical Range and Accuracy**: The complexity and correctness of the grammar used.
    # 3. **Task Achievement**: How well the letter addresses the question, providing relevant arguments and supporting details.
    # 4. **Coherence and Cohesion**: The flow and organization of ideas and the use of transitions between sentences and paragraphs.

    # The letter/application is expected to follow the structure of:
    # - **Sender's Address**: Include all necessary contact details (email, residential address, etc.).
    # - **Date**: The date the letter is written.
    # - **Designation and Address of the Addressee**: Whom the letter is being addressed to.
    # - **Subject**: Clearly state the purpose of the letter.
    # - **Salutation**: Use a formal greeting (e.g., Respected Sir/Ma’am).
    # - **Introduction**: Briefly state the purpose of writing the letter and the issue at hand.
    # - **Body**: Elucidate the details of the issue in clear, concise sentences.
    # - **Conclusion**: Reiterate the purpose of writing the letter, thank the reviewer, and provide a closing salutation.
    # - **Sender’s Name and Designation**: End the letter with the sender’s name and position.

    # The SSC CGL letter is evaluated on the following marking scheme {marking_scheme} with description:
    # - **Relevance**: How well the letter addresses the topic (10 marks).
    # - **Spelling/Grammar**: Accuracy in spelling and grammar (5 marks).
    # - **Word Limit**: Adherence to the word limit in 150-175 words (5 marks). 
    # - **Content Quality**: Depth and clarity of content (8 marks).
    # - **Format**: Proper letter format (5 marks).
    # - **Writing Neatness**: Clarity and neatness of writing (5 marks).
    # - **Effective Sentences**: Use of varied and clear sentence structures (7 marks).
    # - **Cohesiveness**: Logical flow and transitions between ideas (5 marks).

    # Please evaluate the letter based on these criteria. Provide scores for each category, explain why the scores were assigned, and suggest improvements. Also, give an example of a perfect 50-mark answer for the question. The total marks given should be out of 50.
    # Remember if there is nothing like the answer is blank then all scores will be 0 and also remember this strictly that if the answer is not based on the question or is in another direction then also all the scores will be 0. (please evaluate this very strictly)
    
    # Application Question: "{question}"
    # Letter Text: "{letter_text}"

    # *Final Output (Strictly in JSON format with no extra text or comments)*:
    # {{
    #     "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation_for_relevance_score}}"],
    #     "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation_for_spelling_grammar_score}}"],
    #     "Word_Limit_Marks":[{{Word_Limit_Marks}}, "{{Explanation_for_word_limit_score}}"],
    #     "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation_for_content_quality_score}}"],
    #     "Format_Marks": [{{Format_Marks}}, "{{Explanation_for_format_score}}"],
    #     "Writing_Neatness_Marks":[{{Writing_Neatness_Marks}}, "{{Explanation_for_writing_neatness_score}}"],
    #     "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation_for_effective_sentences_score}}"],
    #     "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation_for_cohesiveness_score}}"],
    #     "Total_Marks": [{{Total_Marks}}, "{{Explanation_for_Total_Marks}}"],
    #     "Strengths": "[List of strengths from the user's answer]",
    #     "Weaknesses": "[List of weaknesses from the user's answer that need improvement]",
    #     "50_Marks_Answer": "[Generate a 50-mark answer for the letter writing question of SSC CGL descriptive part, ensuring it addresses all marking criteria comprehensively, with '100-150 words' in response to {question}]",
    #     "AI_Suggestions": "[Provide actionable suggestions to improve the user's answer: {letter_text}, based on the evaluation criteria. Include specific recommendations for improving grammar, clarity, coherence, structure, and task achievement.]",
    #     "Improved_Solution": "[Refine the user's answer: {letter_text}, based on the application question asked, improving areas such as grammar, vocabulary, structure, flow, and content depth while keeping the user’s original tone and intent. The solution should aim for full marks, addressing all evaluation criteria.]"
    # }}
    # """

    prompt = f"""
    You are an experienced examiner tasked with evaluating formal and informal letters written for the SSC CGL descriptive writing test. Your role is to assess the provided letter based on specific marking criteria, ensuring adherence to the proper format and structure. Follow these instructions to evaluate the letter consistently, fairly, and objectively.

    ### Letter Writing Format (For Formal Letters):
    1. **Sender’s Address**: Includes email, residential address, or contact details.
    2. **Date**: Mention the date in DD/MM/YY or MM/DD/YY format.
    3. **Receiver’s Designation and Address**: Include the name/designation and full address of the recipient.
    4. **Subject**: A brief subject line summarizing the purpose (6-8 words).
    5. **Salutation**: Use a formal greeting (e.g., "Respected Sir/Ma’am").
    6. **Body**:
    - **Introduction**: State the purpose of the letter briefly.
    - **Main Content**: Elaborate on the issue with clear, crisp sentences. Provide details, examples, or evidence as necessary.
    - **Conclusion**: Reiterate the purpose and include a polite closing note.
    7. **Closing Line**: Use formal phrases like "Yours sincerely" or "Yours truly."
    8. **Sender’s Name and Designation**: Mention the sender’s details at the end.

    ### Letter Writing Format (For Informal Letters):
    1. **Address**: Include only the sender’s address.
    2. **Date**: Mention the date in DD/MM/YY or MM/DD/YY format.
    3. **Salutation**: Use casual greetings like "Dear [Name]" or "Dearest [Name]."
    4. **Body**:
    - **Introduction**: Set a friendly tone and state the reason for writing.
    - **Main Content**: Share personal experiences, advice, or news.
    - **Conclusion**: End with warm wishes or expressions of affection.
    5. **Closing Line**: Use informal phrases like "Yours lovingly" or "Best wishes."
    6. **Sender’s Name**: Sign off with the sender’s name or nickname.

    ### Evaluation Criteria:
    The letter will be scored on the following criteria:
    1. **Content**: Relevance and adequacy of the information provided in the letter and also if answer is null then its should be scored 0.
    2. **Organization**: Proper adherence to the structure and logical flow of ideas.
    3. **Language and Vocabulary**: Appropriateness and effectiveness of language.
    4. **Coherence and Cohesion**: Logical connection between sentences and paragraphs.
    5. **Contextual Relevance**: Focus and alignment with the letter's purpose.
    6. **Word Limit**: Adherence to the specified word limit (150 words).

    ### Scoring Rules:
    1. **Zero for Blank or Fully Irrelevant Answers**: STRICTLY Award zero marks only if the letter is blank or entirely irrelevant to the topic.
    2. **Partial Scoring for Mixed Relevance**: If some sentences are relevant and others are not, assign marks based on the relevant portions without penalizing heavily for minor mistakes.
    3. **Full Marks for High-Quality Answers**: Award full 50 marks for answers that are almost perfect, with only minor errors or omissions. Do not deduct marks for insignificant issues.

    ### Marking Scheme:
    - **Relevance**: 10 marks
    - **Spelling and Grammar**: 5 marks
    - **Word Limit**: 5 marks
    - **Content Quality**: 8 marks
    - **Format**: 5 marks
    - **Writing Neatness**: 5 marks
    - **Effective Sentences**: 7 marks
    - **Cohesiveness**: 5 marks

    ### Difficulty Level: {difficulty_type}
    This evaluation uses a difficulty level of "{difficulty_type}" to calibrate the strictness of evaluation and the depth of content expected.
    
    ### Evaluation Instructions:
    1. **Strict Scoring for Errors**: Evaluate strictly but fairly, and justify all deductions.
    2. **Constructive Feedback**: Highlight strengths, weaknesses, and specific suggestions for improvement.
    3. **Perfect Letter Example**: Create a 50-marks model letter for the topic.
    4. **Refinement of User Answer**: Revise the user's letter to show how it can achieve a full 50-mark score while retaining its intent.

    ### Expected Output (JSON Format Only):
    Provide the evaluation in the following format:

    {{
        "Relevance_Marks": [{{Relevance_Marks}}, "{{Explanation for relevance score}}"],
        "Spelling_Grammar_Marks": [{{Spelling_Grammar_Marks}}, "{{Explanation for spelling and grammar score}}"],
        "Word_Limit_Marks": [{{Word_Limit_Marks}}, "{{Explanation for word limit score}}"],
        "Content_Quality_Marks": [{{Content_Quality_Marks}}, "{{Explanation for content quality score}}"],
        "Format_Marks": [{{Format_Marks}}, "{{Explanation for format score}}"],
        "Writing_Neatness_Marks": [{{Writing_Neatness_Marks}}, "{{Explanation for writing neatness score}}"],
        "Effective_Sentences_Marks": [{{Effective_Sentences_Marks}}, "{{Explanation for effective sentences score}}"],
        "Cohesiveness_Marks": [{{Cohesiveness_Marks}}, "{{Explanation for cohesiveness score}}"],
        "Total_Marks": [{{Total_Marks}}, "{{Summary of overall evaluation}}"],
        "Strengths": "[List of strengths in the user's letter]",
        "Weaknesses": "[List of weaknesses and areas of improvement]",
        "50_Marks_Answer": "[Provide a model letter for the question: {question}, that demonstrates a perfect score based on all evaluation criteria.]",
        "AI_Suggestions": "[List specific suggestions to improve the user's letter based on evaluation criteria.]",
        "Improved_Solution": "[Provide a revised version of the user's letter: {letter_text}, that addresses weaknesses and demonstrates how to achieve a full 50-mark score.]"
    }}

    **Letter Question**: "{question}"  
    **Letter Text**: "{letter_text}"
    """

    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        # Extract the response and process it
        cleaned_content = clean_invalid_chars(response.choices[0].message.content.strip())
        evaluation_result, parse_error = safe_json_parse(cleaned_content)

        result = {
            "Word_Count": len(letter_text.split()),
            "Relevance_Marks": "N/A",
            "Spelling_Grammar_Marks": "N/A",
            "Word_Limit_Marks": "N/A",
            "Content_Quality_Marks": "N/A",
            "Format_Marks": "N/A",
            "Writing_Neatness_Marks": "N/A",
            "Effective_Sentences_Marks": "N/A",
            "Cohesiveness_Marks": "N/A",
            "Total_Marks": "N/A",
            "Strengths": "N/A",
            "Weaknesses": "N/A",
            "50_Marks_Answer": "N/A",
            "AI_Suggestions": "N/A",
            "Improved_Solution": "N/A"
        }

        if parse_error:
            print(f"JSON parsing error: {parse_error}")
            result["raw_response"] = cleaned_content

        # Populate result fields
        for key in result.keys():
            if key in evaluation_result:
                result[key] = evaluation_result.get(key, "N/A")
        
        print(result)
        return result

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return {
            "error": "Invalid response format from AI model",
            "raw_response": cleaned_content,
            "Relevance_Marks": "N/A",
            "Spelling_Grammar_Marks": "N/A",
            "Word_Limit_Marks": "N/A",
            "Content_Quality_Marks": "N/A",
            "Format_Marks": "N/A",
            "Writing_Neatness_Marks": "N/A",
            "Effective_Sentences_Marks": "N/A",
            "Cohesiveness_Marks": "N/A",
            "Total_Marks": "N/A",
            "Strengths": "N/A",
            "Weaknesses": "N/A",
            "50_Marks_Answer": "N/A",
            "AI_Suggestions": "N/A",
            "Improved_Solution": "N/A"
        }

    except Exception as e:
        return {"error": f"An error occurred while processing the request: {str(e)}"}



