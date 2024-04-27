__all__ = ["languague", "create_animation", "get_language"]


def create_animation() -> str:
    """Create a simple animation using JavaScript"""
    return """
    function createGradioAnimation() {
        var container = document.createElement('div');
        container.id = 'gradio-animation';
        container.style.fontSize = '2em';
        container.style.fontWeight = 'bold';        
        container.style.textAlign = 'center';
        container.style.marginBottom = '20px';

        var text = '🐉 Welcome to Lumina ☀️';
        for (var i = 0; i < text.length; i++) {
            (function(i){
                setTimeout(function(){
                    var letter = document.createElement('span');
                    letter.style.opacity = '0';
                    letter.style.transition = 'opacity 0.5s';
                    letter.innerText = text[i];
                    letter.style.color = "hsl(" + (i * 360 / text.length) + ", 70%, 55%)";
                    container.appendChild(letter);
                    setTimeout(function() {
                        letter.style.opacity = '1';
                    }, 50);
                }, i * 250);
            })(i);
        }

        var gradioContainer = document.querySelector('.gradio-container');
        gradioContainer.insertBefore(container, gradioContainer.firstChild);

        return 'Animation created';
    }
    """


languages = {
    "Arabic": "ar",
    "Simplified Chinese": "ch_sim",
    "Traditional Chinese": "ch_tra",
    "German": "de",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Thai": "th",
    "Vietnamese": "vi",
}


def get_language(lang) -> str:
    """Get the list of supported languages"""
    return languages[lang]
