from flask import Flask, render_template, request, send_from_directory
import json
import os

app = Flask(__name__, instance_relative_config=True)

def load_json_data(filename):
    """
    Utility function to load JSON data from the data folder.
    """
    with open(os.path.join('data', filename)) as f:
        return json.load(f)

# Load data from JSON files
projects = load_json_data('projects.json')
testimonials = load_json_data('testimonials.json')
timeline_data = load_json_data('timeline.json')
blog_posts = load_json_data('blog_posts.json')
skills_data = load_json_data('skills.json')
achievements = load_json_data('achievements.json')

@app.route('/')
def index():
    """
    Home page - showcases About snippet, featured projects, skills preview,
    video intro, sample testimonials, achievements, and resume links.
    """
    # Show a subset of projects on the homepage as featured
    featured_projects = projects[:4]
    # Show a few testimonials on homepage
    featured_testimonials = testimonials[:3]
    return render_template(
        'index.html',
        projects=featured_projects,
        testimonials=featured_testimonials,
        skills=skills_data,
        achievements=achievements,
        title="Home - Personal Portfolio"
    )

@app.route('/about')
def about():
    """
    About page - more detailed biography, profile image, and social links.
    """
    return render_template('about.html', title="About Me")

@app.route('/projects')
def project_gallery():
    """
    Projects page - displays full project gallery with client-side filtering.
    """
    return render_template(
        'projects.html',
        projects=projects,
        title="Projects"
    )

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    """
    Case study page for an individual project.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', project=project, title=project['title'])
    return "Project not found", 404

@app.route('/skills')
def skills():
    """
    Skills page - displays technical skills with progress bars.
    """
    return render_template('skills.html', skills=skills_data, title="Skills")

@app.route('/testimonials')
def testimonials_page():
    """
    Testimonials page - displays all testimonials in a carousel-like layout.
    """
    return render_template('testimonials.html', testimonials=testimonials, title="Testimonials")

@app.route('/testimonial/submit', methods=['GET', 'POST'])
def submit_testimonial():
    """
    Form to submit new testimonials. In a real scenario, this would store data in a DB.
    Here we just simulate by appending to an array.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')
        message = request.form.get('message')
        # In production, validate and store in DB
        new_testimonial = {
            "name": name,
            "role": role,
            "message": message,
            "image": "images/default.png"
        }
        testimonials.append(new_testimonial)
        return render_template('submit_testimonial.html', success=True, title="Submit Testimonial")
    return render_template('submit_testimonial.html', title="Submit Testimonial")

@app.route('/contact', methods=['GET','POST'])
def contact():
    """
    Contact form page - allows visitors to send messages.
    In production, you'd send emails or store in a DB.
    """
    if request.method == 'POST':
        # Process form (send email or store message)
        return render_template('contact.html', success=True, title="Contact")
    return render_template('contact.html', title="Contact")

@app.route('/timeline')
def timeline():
    """
    Timeline page - displays career or project milestones.
    """
    return render_template('timeline.html', timeline=timeline_data, title="Timeline")

@app.route('/blog')
def blog():
    """
    Blog page - lists blog posts with excerpts and links.
    """
    return render_template('blog.html', posts=blog_posts, title="Blog")

@app.route('/resume')
def resume():
    """
    Resume page - interactive resume viewer using embedded PDF.
    """
    return render_template('resume.html', title="Resume")

@app.route('/download_resume')
def download_resume():
    """
    Download route for the resume PDF file.
    """
    return send_from_directory('static/pdf', 'resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
