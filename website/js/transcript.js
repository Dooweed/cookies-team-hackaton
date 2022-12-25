let scheduledTranscript = null;

function playTranscript(transcript, index) {
    const currentTime = player.getCurrentTime();
    let {audio, text, dur, ...rest} = transcript[index];

    const snd = new Audio("data:audio/wav;base64," + audio);
    snd.play();
    console.log(text);
    console.log(player.getCurrentTime(), transcript[index].start)

    if(index + 1 < transcript.length) {
        const start = parseFloat(transcript[index + 1].start);

        scheduledTranscript = setTimeout(playTranscript, (start - currentTime) * 1000, transcript, index + 1)
    }
}
