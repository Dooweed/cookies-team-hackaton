let scheduledTranscript = null;

function playTranscript(transcript, index) {
    const currentTime = player.getCurrentTime();
    let {audio, text, dur, ...rest} = transcript[index];
    let playbackRate = 1;

    const snd = new Audio("data:audio/wav;base64," + audio);
    if(snd > dur)
        playbackRate = snd.duration / dur;
    snd.playbackRate = playbackRate;
    snd.play();
    console.log(text);
    console.log('Rate: ', snd.duration, 'dur', dur, 'Current time: ', player.getCurrentTime(), 'Original time: ', transcript[index].start)

    if(index + 1 < transcript.length) {
        const start = parseFloat(transcript[index + 1].start);

        scheduledTranscript = setTimeout(playTranscript, (start - currentTime) * 1000, transcript, index + 1)
    }
}
