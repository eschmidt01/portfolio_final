document.addEventListener('DOMContentLoaded', function () {
    // Project Filtering
    const filters = document.querySelectorAll('.filter-bar button');
    const projects = document.querySelectorAll('.project-card');

    filters.forEach(filter => {
        filter.addEventListener('click', () => {
            const filterValue = filter.getAttribute('data-filter');

            projects.forEach(project => {
                const skills = project.getAttribute('data-skills');
                if (filterValue === 'all' || skills.includes(filterValue)) {
                    project.style.display = 'block';
                } else {
                    project.style.display = 'none';
                }
            });

            // Highlight active filter
            filters.forEach(f => f.classList.remove('active'));
            filter.classList.add('active');
        });
    });

    // Smooth scroll for Testimonials
    const carousel = document.querySelector('.testimonials-carousel');
    if (carousel) {
        carousel.addEventListener('wheel', (e) => {
            e.preventDefault();
            carousel.scrollBy({
                left: e.deltaY < 0 ? -300 : 300,
                behavior: 'smooth',
            });
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        // Animate progress bars
        const progressBars = document.querySelectorAll('.progress');
    
        progressBars.forEach((bar) => {
            const skillLevel = bar.dataset.skillLevel;
            bar.style.width = `${skillLevel}%`;
        });
    });
    
    
});
