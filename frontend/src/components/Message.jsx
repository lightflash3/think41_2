import React from 'react';

export default function Message({ role, text }) {
  const isUser = role === 'user';
  return (
    <div className={`mb-2 ${isUser ? 'text-right' : 'text-left'}`}>
      <span className={`inline-block px-4 py-2 rounded-xl ${isUser ? 'bg-blue-500 text-white' : 'bg-gray-300 text-black'}`}>
        {text}
      </span>
    </div>
  );
}
