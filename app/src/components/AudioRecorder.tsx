import React, { useState, useRef } from 'react';
import MicIcon from '@mui/icons-material/Mic';


const AudioRecorder: React.FC = () => {
    const [isRecording, setIsRecording] = useState(false);
    const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
    const mediaRecorderRef = useRef<MediaRecorder | null>(null);
    const [isButtonPressed, setIsButtonPressed] = useState(false);

    const buttonColor = isButtonPressed ? 'bg-blue-500' : 'bg-green-500';

    const handleStartRecording = () => {
        setIsButtonPressed(true);

        navigator.mediaDevices.getUserMedia({ audio: true })
            .then((stream) => {
                const mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.ondataavailable = (event) => {
                    if (event.data.size > 0) {
                        setAudioBlob(event.data);
                    }
                };

                mediaRecorder.onstop = () => {
                    stream.getTracks().forEach(track => track.stop());
                };

                mediaRecorderRef.current = mediaRecorder;
                mediaRecorder.start();
                setIsRecording(true);
            })
            .catch((error) => {
                console.error('Error accessing microphone:', error);
            });
    };

    const handleStopRecording = () => {
        setIsButtonPressed(false);

        if (mediaRecorderRef.current) {
            mediaRecorderRef.current.stop();
            setIsRecording(false);
        }
    };

    const handleStartTouchRecording = (event: React.TouchEvent) => {
        event.preventDefault();
        handleStartRecording();
    };

    const handleStopTouchRecording = (event: React.TouchEvent) => {
        event.preventDefault();
        handleStopRecording();
    };

    return (
        <div className=' grid grid-cols-1 items-center gap-5'>
            <div className='flex justify-center'>
                <button
                    className={`text-white px-4 py-2 ${buttonColor} select-none`}
                    onTouchStart={handleStartTouchRecording}
                    onTouchEnd={handleStopTouchRecording}
                    onMouseDown={handleStartRecording}
                    onMouseUp={handleStopRecording}
                >
                    <MicIcon></MicIcon>
                </button>
            </div>

            <div className='flex justfiy-center'>

                {audioBlob && (
                    <audio controls>
                        <source src={URL.createObjectURL(audioBlob)} type="audio/wav" />
                        Your browser does not support the audio element.
                    </audio>
                )}
            </div>
        </div>
    );
};

export default AudioRecorder;
