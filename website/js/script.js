(() => {
    const form = document.querySelector('form#form'),
        linkInput = document.querySelector('input#link');
    const serverUrl = 'http://localhost:5000/api/transcript';

    form.addEventListener('submit', async e => {
        const videoId = /https:\/\/www.youtube.com\/watch\?v=([a-zA-Z0-9]{3,})&?.*/g
            .exec(linkInput.value)[1];
        e.preventDefault();

        const response = await fetch(serverUrl + '?' + new URLSearchParams({'link': linkInput.value}));
        response.json().then((data) => {
            console.log('Data received', data);

            if(player) {
                const playerElement = document.querySelector('#player');
                playerElement.parentNode.replaceChild(
                    document.createElement('<div class="player" id="player"></div>'),
                    playerElement
                )
            }
            loadYoutubePlayer(videoId);

            player.addEventListener('onStateChange', function (e) {
                // Run transcripting and detach event listener
                if (e.data === YT.PlayerState.PLAYING) {
                    resumeTranscript();
                    stopTranscript();

                    const currentTime = player.getCurrentTime();
                    let startIndex = 0;
                    while (parseFloat(data[startIndex].start) < currentTime) {
                        startIndex++;
                    }
                    const start = parseFloat(data[startIndex].start);
                    scheduledTranscript = setTimeout(playTranscript, (start - currentTime) * 1000, data, startIndex);
                }
            })

            player.addEventListener('onStateChange', (e) => {
                console.log('SC', e.data);
                switch (e.data) {
                    case YT.PlayerState.PAUSED:
                        stopTranscript();
                        break;
                }
            })
            scrollToEl('player');
        });
    })
})()