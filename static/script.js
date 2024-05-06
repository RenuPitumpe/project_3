document.addEventListener("DOMContentLoaded", function() {
    const submitButton = document.getElementById("submit-button");
    const analysisResults = document.getElementById("analysis-results");

    submitButton.addEventListener("click", function() {
        const title = document.getElementById("movie-title").value;
        const year = document.getElementById("release-year").value;
        const genre = document.getElementById("genre").value;

        if (title && year && genre) {
            // Simple analysis: Display movie details
            const analysis = `
                <p><strong>Title:</strong> ${title}</p>
                <p><strong>Release Year:</strong> ${year}</p>
                <p><strong>Genre:</strong> ${genre}</p>
            `;
            analysisResults.innerHTML = analysis;
        } else {
            alert("Please fill in all fields.");
        }
    });
});
