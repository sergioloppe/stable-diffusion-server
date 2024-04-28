import React, { useState } from 'react';
import styles from './PromptInput.module.css';

function PromptInput() {
  const baseUrl = window.location.origin;
  const [prompt, setPrompt] = useState('');
  const [generatedImageBase64, setGeneratedImageBase64] = useState(
    'data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=',
  );

  const submitButton = (e) => {
    e.preventDefault(); // Prevent the default form submission behavior
    console.log('Sending prompt:', prompt);

    fetch(baseUrl + '/api/inference', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt: prompt }),
    })
      .then((response) => {
        if (response.ok) {
          return response.blob();
        }
        throw new Error('Network response was not ok.');
      })
      .then((blob) => {
        const reader = new FileReader();
        reader.onloadend = () => {
          setGeneratedImageBase64(reader.result);
        };
        reader.readAsDataURL(blob);
      })
      .catch((error) => {
        console.error('Fetching error:', error);
      });
  };

  return (
    <div className={styles.container}>
      <form onSubmit={submitButton} className={styles.form}>
        <label className={styles.label}>
          Prompt:
          <input
            type='text'
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            name='prompt'
            className={styles.input}
          />
        </label>
        <button type='submit' className={styles.button}>
          Submit
        </button>
        <img src={generatedImageBase64} alt='Generated' className={styles.image} />
      </form>
    </div>
  );
}

export default PromptInput;
