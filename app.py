from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded career data (simulating PDF's job market analysis)
careers = {
    'Data Scientist': {'required_skills': ['Python', 'Data Analysis', 'Machine Learning'], 'match_threshold': 2},
    'Software Engineer': {'required_skills': ['Python', 'Java', 'Problem Solving'], 'match_threshold': 1},
    'Project Manager': {'required_skills': ['Communication', 'Leadership', 'Teamwork'], 'match_threshold': 2}
}

# Hardcoded learning resources (simulating curated recommendations)
resources = {
    'Data Scientist': ['Python for Data Science on Coursera', 'Machine Learning Certification on Google Cloud'],
    'Software Engineer': ['Intro to Java on Udemy', 'Problem Solving with Algorithms book'],
    'Project Manager': ['Communication Skills Workshop on LinkedIn Learning', 'Leadership Certification on edX']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hard_skills = request.form['hard_skills'].split(',')
        soft_skills = request.form['soft_skills'].split(',')
        interests = request.form['interests']
        
        # Clean up lists
        hard_skills = [skill.strip() for skill in hard_skills if skill.strip()]
        soft_skills = [skill.strip() for skill in soft_skills if skill.strip()]
        
        all_skills = hard_skills + soft_skills
        
        # Generate skill profile
        skill_profile = {
            'hard': hard_skills,
            'soft': soft_skills,
            'interests': interests
        }
        
        # Recommend careers
        recommendations = []
        for career, data in careers.items():
            match_count = sum(1 for skill in data['required_skills'] if skill in all_skills)
            if match_count >= data['match_threshold']:
                match_percent = (match_count / len(data['required_skills'])) * 100
                recommendations.append(f"{career} - {int(match_percent)}% Match")
        
        if not recommendations:
            recommendations = ['No strong matches - try adding more skills!']
        
        # Suggest learning resources based on top recommendation
        suggestions = []
        if recommendations:
            top_career = recommendations[0].split(' - ')[0]
            suggestions = resources.get(top_career, ['General: Explore free courses on Khan Academy'])
        
        return render_template('result.html', profile=skill_profile, recs=recommendations, suggs=suggestions)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
