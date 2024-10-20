import React from 'react';
import Chat from './components/chat'

const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-4xl font-bold text-center mb-8">Welcome to the Chat App</h1>
      <div className="flex justify-center">
        {/* Render the Chat component */}
        <Chat />
      </div>
    </div>
  );
};

export default Home;