let scheduledTranscript = null, pausedTime, sound;

function playTranscript(transcript, index) {
    clearTimeout(scheduledTranscript);
    const currentTime = player.getCurrentTime();
    let {audio, audio_duration, text, dur, ...rest} = transcript[index];
    let interTranscriptDuration;
    let playbackRate = 1;

    if(transcript.length <= index) {
        interTranscriptDuration = 1000
    } else {
        interTranscriptDuration = transcript[index + 1].start  - transcript[index].start
    }

    sound = new Audio("data:audio/wav;base64," + audio);
    if(audio_duration > interTranscriptDuration)
        playbackRate = audio_duration / interTranscriptDuration;
    sound.playbackRate = playbackRate;
    sound.volume;
    sound.play();

    console.log(text);
    console.log('Rate: ', playbackRate, audio_duration, interTranscriptDuration, 'Current time: ', player.getCurrentTime(), 'Original time: ', transcript[index].start)

    if(index + 1 < transcript.length) {
        const start = parseFloat(transcript[index + 1].start);

        scheduledTranscript = setTimeout(playTranscript, (start - currentTime) * 1000, transcript, index + 1)
    }
}

function stopTranscript(){
    clearTimeout(scheduledTranscript);
    if(sound) {
        sound.pause();
        pausedTime = player.getCurrentTime();
    }
}

function resumeTranscript() {
    console.log(pausedTime, player.getCurrentTime())
    if(Math.abs(pausedTime - player.getCurrentTime()) < 0.3)
        sound.play();
}
