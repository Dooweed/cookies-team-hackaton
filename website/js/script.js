(() => {
    const form = document.querySelector('form#form');
    const serverUrl = 'http://localhost:5000/api/transcript';

    form.addEventListener('submit', async e => {
        const videoId = /https:\/\/www.youtube.com\/watch\?v=([a-zA-Z0-9]{3,})&?.*/g
            .exec('https://www.youtube.com/watch?v=M7FIvfx5J10&asd=asdsds')[1];
        e.preventDefault();

        const response = await fetch(serverUrl + '?' + new URLSearchParams(new FormData(form).entries()));
        response.json().then((data) => {
            console.log('Data received', data);

            loadYoutubePlayer(videoId);

            player.addEventListener('onStateChange', function (e) {
                // Run transcripting and detach event listener
                if (e.data === YT.PlayerState.PLAYING) {
                    setTimeout(playTranscript, data[0].start * 1000, data, 0);
                    player.removeEventListener('onStateChange', this);
                }
            })
        });
    })
})()