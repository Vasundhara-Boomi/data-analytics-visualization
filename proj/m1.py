import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample learner-course matrix (binary: 1 if taken, 0 if not)
learner_courses = np.array([
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1],
])

# Function to recommend courses to a learner
def recommend_courses(learner_id, num_recommendations=3):
    learner_vector = learner_courses[learner_id]
    similarities = cosine_similarity(learner_courses)
    similar_learners = np.argsort(similarities[learner_id])[::-1]  # Sort by similarity, descending

    recommended_courses = []

    for similar_learner in similar_learners:
        if similar_learner == learner_id:
            continue  # Skip the same learner

        similar_learner_vector = learner_courses[similar_learner]
        new_courses = np.where(learner_vector == 0)[0]  # Find courses not taken by the learner

        for course in new_courses:
            if similar_learner_vector[course] == 1 and course not in recommended_courses:
                recommended_courses.append(course)

                if len(recommended_courses) >= num_recommendations:
                    return recommended_courses

    return recommended_courses

# User Interface
while True:
    try:
        learner_id = int(input("Enter your learner ID (0-3) or -1 to exit: "))
        if learner_id == -1:
            break
        if learner_id < 0 or learner_id >= learner_courses.shape[0]:
            print("Invalid learner ID. Please enter a valid learner ID.")
        else:
            recommended_courses = recommend_courses(learner_id, num_recommendations=3)
            print(f"Recommended courses for learner {learner_id}: {recommended_courses}")
    except ValueError:
        print("Invalid input. Please enter a valid learner ID.")