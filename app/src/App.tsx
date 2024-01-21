import React from 'react';
import AudioRecorder from './components/AudioRecorder';
import Chat from './components/Chat';

function App() {

  return (
    <div>
      <div className='flex bg-slate-500 h-screen justify-center items-center'>
        <div>
          <Chat></Chat>
          <AudioRecorder />
        </div>
      </div>
    </div>
  );
}

export default App;
