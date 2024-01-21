import React, { useState } from 'react';
import AudioRecorder from './AudioRecorder';
import SendIcon from '@mui/icons-material/Send';
import { fetchChatbotResponse, sendOpusBlobToBackend } from './API';
import IosShareIcon from '@mui/icons-material/IosShare';

const Chat: React.FC = () => {
    const [inputValue, setInputValue] = useState<string>('');
    const [messages, setMessages] = useState<string[]>([]);
    const [audioBlob, setAudioBlob] = useState<Blob | null>(null);


    const handleSendMessage = () => {
        if (inputValue.trim() !== '') {
            setMessages([...messages, inputValue]);
            let res = fetchChatbotResponse(inputValue)
            setInputValue('');
            res.then((data) => {
                setMessages([...messages, data.result])
            })
        }
    };

    const handelSendAudio = (blob: Blob) => {
        setAudioBlob(blob)
        sendOpusBlobToBackend(blob)
        console.log(blob)
    }

    return (
        <div className="w-screen mx-auto p-4 justify-center">
            <div className='flex w-full gap-2'>
                <div className="w-[85%]">
                    <input
                        type="text"
                        className="border p-2 w-full"
                        placeholder="Type your message..."
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                    />
                </div>
                <div className="flex justify-center">
                    <button
                        className="bg-blue-500 text-white px-4 py-2"
                        onClick={handleSendMessage}
                    >
                        <SendIcon></SendIcon>
                    </button>
                </div>
                <div>
                    <AudioRecorder handleSendAudio={handelSendAudio}
                    ></AudioRecorder>
                </div>
                <div>
                    <button className="bg-red-500 text-white px-4 py-2">
                        <IosShareIcon></IosShareIcon>
                    </button>
                </div>
            </div>
            <div>
                <h3 className="text-lg font-semibold mb-2">Messages:</h3>
                <ul>
                    {messages.map((message, index) => (
                        <li key={index} className="mb-1">{message}</li>
                    ))}
                </ul>
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

export default Chat;
