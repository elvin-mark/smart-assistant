import React, { useState } from 'react';
import AudioRecorder from './AudioRecorder';
import SendIcon from '@mui/icons-material/Send';
import { fetchChatbotResponse } from './API';

const Chat: React.FC = () => {
    const [inputValue, setInputValue] = useState<string>('');
    const [messages, setMessages] = useState<string[]>([]);

    const handleSend = () => {
        if (inputValue.trim() !== '') {
            setMessages([...messages, inputValue]);
            let res = fetchChatbotResponse(inputValue)
            setInputValue('');
            res.then((data) => {
                setMessages([...messages, data.result])
            })
        }
    };

    return (
        <div className="w-screen mx-auto p-4 justify-center">
            <div className='flex grid grid-cols-4 gap-2'>
                <div className="col-span-3">
                    <input
                        type="text"
                        className="border p-2 w-full"
                        placeholder="Type your message..."
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                    />
                </div>
                <div className="">
                    <button
                        className="bg-blue-500 text-white px-4 py-2"
                        onClick={handleSend}
                    >
                        <SendIcon></SendIcon>
                    </button>
                </div>
                {/* <AudioRecorder></AudioRecorder> */}
            </div>
            <div>
                <h3 className="text-lg font-semibold mb-2">Messages:</h3>
                <ul>
                    {messages.map((message, index) => (
                        <li key={index} className="mb-1">{message}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Chat;
