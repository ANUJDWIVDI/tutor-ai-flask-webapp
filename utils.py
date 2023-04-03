from flask import Flask, render_template, request
import pandas as pd


questions = [
    {
        "question": "What is the definition of artificial intelligence?",
        "options": [
            {"option": "The ability of a machine to perform tasks that require human-like intelligence",
             "scores": [8, 7, 9, 6, 5]},
            {"option": "The ability of a machine to understand natural language", "scores": [7, 8, 7, 8, 6]},
            {"option": "The ability of a machine to perform repetitive tasks", "scores": [5, 6, 5, 7, 8]},
            {"option": "The ability of a machine to recognize images", "scores": [6, 5, 8, 7, 7]}
        ]
    },
    {
        "question": "Which of the following is an example of supervised learning?",
        "options": [
            {"option": "Training a machine learning algorithm to identify different types of fruit in images",
             "scores": [8, 7, 9, 6, 5]},
            {
                "option": "Using an unsupervised learning algorithm to group similar customers together based on their purchasing history",
                "scores": [7, 8, 7, 8, 6]},
            {"option": "Teaching a machine learning algorithm to play chess by playing against itself", "scores": [
                5, 6, 5, 7, 8]},
            {"option": "Using a machine learning algorithm to generate new images based on existing ones", "scores":
                [6, 5, 8, 7, 7]}
        ]
    },
    {
        "question": "What is the purpose of reinforcement learning?",
        "options": [
            {"option": "To teach a machine to recognize patterns in data", "scores": [5, 6, 5, 7, 8]},
            {"option": "To allow a machine to learn from its mistakes and adjust its behavior accordingly", "scores":
                [8, 7, 9, 6, 5]},
            {"option": "To group similar items together based on their attributes", "scores": [7, 8, 7, 8, 6]},
            {"option": "To generate new data based on existing data", "scores": [6, 5, 8, 7, 7]}
        ]
    },
    {
        "question": "Which of the following is an example of a neural network architecture?",
        "options": [
            {"option": "Convolutional neural network", "scores": [8, 7, 9, 6, 5]},
            {"option": "Support vector machine", "scores": [7, 8, 7, 8, 6]},
            {"option": "Decision tree", "scores": [5, 6, 5, 7, 8]},
            {"option": "K-means clustering", "scores": [6, 5, 8, 7, 7]}
        ]
    },
    {
        "question": "What is the purpose of a loss function in machine learning?",
        "options": [
            {"option": "To measure the accuracy of the model's predictions", "scores": [8, 7, 9, 6, 5]},
            {"option": "To optimize the model's parameters during training", "scores": [7, 8, 7, 8, 6]},
            {"option": "To prevent overfitting of the model to the training data", "scores": [5, 6, 5, 7, 8]},
            {"option": "To preprocess the input data before feeding it into the model", "scores": [6, 5, 8, 7, 7]}]
    },
    {
        "question": "Which of the following is a commonly used programming language for machine learning?",
        "options": [
            {"option": "Java", "scores": [6, 5, 8, 7, 7]},
            {"option": "Python", "scores": [8, 7, 9, 6, 5]},
            {"option": "C#", "scores": [5, 6, 5, 7, 8]},
            {"option": "Ruby", "scores": [7, 8, 7, 8, 6]}]
    },
    {
        "question": "Which of the following is not a type of machine learning algorithm?",
        "options": [
            {"option": "Supervised learning", "scores": [8, 7, 9, 6, 5]},
            {"option": "Reinforcement learning", "scores": [7, 8, 7, 8, 6]},
            {"option": "Unsupervised learning", "scores": [5, 6, 5, 7, 8]},
            {"option": "Descending learning", "scores": [6, 5, 8, 7, 7]}]
    },
    {
        "question": "Which of the following is an example of unsupervised learning?",
        "options": [
            {"option": "Predicting the likelihood of a customer purchasing a product", "scores": [5, 6, 5, 7, 8]},
            {"option": "Identifying whether an image contains a cat or a dog ", "scores": [6, 5, 8, 7, 7]},
            {"option": "Clustering similar documents together", "scores": [8, 7, 9, 6, 5]},
            {"option": "Recommending a movie based on a user's past viewing history", "scores": [7, 8, 7, 8, 6]}]
    },
    {
        "question": "Which of the following is a commonly used neural network activation function?",
        "options": [
            {"option": "Linear activation", "scores": [5, 6, 5, 7, 8]},
            {"option": "Sigmoid activation", "scores": [8, 7, 9, 6, 5]},
            {"option": "Softmax activation", "scores": [7, 8, 7, 8, 6]},
            {"option": "ReLU activation", "scores": [6, 5, 8, 7, 7]}]
    },
    {
        "question": "What is the purpose of the test set in machine learning?",
        "options": [
            {"option": "To measure the accuracy of the model on new, unseen data", "scores": [8, 7, 9, 6, 5]},
            {"option": "To fine-tune the model's parameters during training", "scores": [7, 8, 7, 8, 6]},
            {"option": "To prevent overfitting of the model to the training data", "scores": [5, 6, 5, 7, 8]},
            {"option": "To generate new data based on existing data", "scores": [6, 5, 8, 7, 7]}]
    },
    {
        "question": "Which of the following is a commonly used machine learning framework?",
        "options": [
            {"option": "TensorFlow", "scores": [8, 7, 9, 6, 5]},
            {"option": "JQuery", "scores": [5, 6, 5, 7, 8]},
            {"option": "Django", "scores": [6, 5, 8, 7, 7]},
            {"option": "Ruby on Rails", "scores": [7, 8, 7, 8, 6]}]
    },
    {
        "question": "Which of the following is a commonly used evaluation metric for binary classification problems?",
        "options": [
            {"option": "Mean squared error", "scores": [5, 6, 5, 7, 8]},
            {"option": "Precision", "scores": [8, 7, 9, 6, 5]},
            {"option": "F1 score", "scores": [7, 8, 7, 8, 6]},
            {"option": "R squared", "scores": [6, 5, 8, 7, 7]}]
    },
    {
        "question": "What is the difference between artificial intelligence and machine learning?",
        "options": [
            {"option": "AI is a subset of ML", "scores": [5, 7, 6, 8, 7]},
            {"option": "ML is a subset of AI ", "scores": [8, 6, 7, 5, 6]},
            {"option": "AI and ML are the same thing ", "scores": [6, 8, 6, 7, 8]},
            {"option": "R squaredAI and ML are completely unrelated", "scores": [7, 5, 8, 6, 5]}]
    },
    {
        "question": "Which of the following is an example of unsupervised learning?",
        "options": [
            {"option": "Training a machine learning algorithm to identify different types of animals in images ", "scores": [5, 7, 6, 8, 7]},
            {"option": "Using a supervised learning algorithm to classify emails as spam or not spam ", "scores": [8, 6, 7, 5, 6]},
            {"option": "Using an unsupervised learning algorithm to group similar customers together based on their purchasing history", "scores": [6, 8, 6, 7, 8]},
            {"option": "Teaching a machine learning algorithm to play chess by playing against itself ", "scores": [7, 5, 8, 6, 5]}]
    },
    {
        "question": "What is the purpose of convolutional neural networks?",
        "options": [
            {"option": "To classify images",
             "scores": [8, 7, 6, 5, 6]},
            {"option": "To perform natural language processing",
             "scores": [6, 8, 7, 5, 7]},
            {
                "option": "To generate new data based on existing data",
                "scores": [5, 6, 8, 7, 8]},
            {"option": "To group similar items together based on their attributes",
             "scores": [7, 5, 8, 6, 5]}]
    },
    {
        "question": "Which of the following is an example of reinforcement learning?",
        "options": [
            {"option": "Training a machine learning algorithm to identify different types of flowers in images",
             "scores": [8, 7, 6, 5, 6]},
            {"option": "Using an unsupervised learning algorithm to group similar customers together based on their purchasing history",
             "scores": [6, 8, 7, 5, 7]},
            {
                "option": " Teaching a machine learning algorithm to play chess by playing against itself",
                "scores": [5, 6, 8, 7, 8]},
            {"option": "Using a machine learning algorithm to generate new images based on existing ones",
             "scores": [7, 5, 8, 6, 5]}]
    },
    {
        "question": "What is the purpose of transfer learning?",
        "options": [
            {"option": "To transfer knowledge from one machine learning task to another",
             "scores": [8, 7, 6, 5, 6]},
            {"option": "To optimize the model's parameters during training",
             "scores": [6, 8, 7, 5, 7]},
            {
                "option": " To prevent overfitting of the model to the training data",
                "scores": [5, 6, 8, 7, 8]},
            {"option": "To generate new data based on existing data",
             "scores": [7, 5, 8, 6, 5]}]
    },
    {
        "question": "What is the purpose of a deep neural network?",
        "options": [
            {"option": "To perform natural language processing",
             "scores": [8, 7, 6, 5, 6]},
            {"option": "To perform sentiment analysis",
             "scores": [6, 8, 7, 5, 7]},
            {
                "option": "To classify images",
                "scores": [5, 6, 8, 7, 8]},
            {"option": "To generate new data based on existing data",
             "scores": [7, 5, 8, 6, 5]}]
    }

]

def calculate_scores(answers, questions):
    # Initialize a list to keep track of the score for each category
    category_scores = [0, 0, 0, 0, 0]

    for question in questions:
        for option in question["options"]:
            if option["option"] == answers.get(question["question"]):
                # Append the scores for this option to a list
                scores = option["scores"]
                # Add the score values for this option to the corresponding category score
                for i, score in enumerate(scores):
                    if i < len(category_scores):
                        category_scores[i] += score

    # Print the title and score for each category
    category_titles = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]
    for i in range(5):
        print(category_titles[i], ":", category_scores[i])

    # Calculate the total score as a sum of all category scores
    total_score = sum(category_scores)

    # Calculate the percentage score as a fraction of the maximum possible score (sum of all scores)
    max_score = sum([max(option["scores"]) for question in questions for option in question["options"]])
    percentage_score = round((total_score / max_score) * 100)

    # Return the percentage score
    return percentage_score



