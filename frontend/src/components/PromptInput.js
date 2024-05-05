import React, { useState } from 'react';
import styles from './PromptInput.module.css';

function PromptInput() {
  const baseUrl = window.location.origin;
  const [prompt, setPrompt] = useState('');
  const [negativePrompt, setNegativePrompt] = useState('');
  const [width, setWidth] = useState(512);
  const [height, setHeight] = useState(512);
  const [guidanceScale, setGuidanceScale] = useState(7);
  const [numInferenceSteps, setNumInferenceSteps] = useState(20);
  const [seed, setSeed] = useState(0);
  const [generatedImageBase64, setGeneratedImageBase64] = useState(
    'data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=',
  );
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

    try {
      const response = await fetch(baseUrl + '/api/inference', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt,
          negative_prompt: negativePrompt,
          width: width,
          height: height,
          guidance_scale: guidanceScale,
          num_inference_steps: numInferenceSteps,
          seed: seed,
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok.');
      }

      const blob = await response.blob();
      const reader = new FileReader();
      reader.onloadend = () => {
        setGeneratedImageBase64(reader.result);
        setIsLoading(false);
      };
      reader.readAsDataURL(blob);
    } catch (error) {
      console.error('Fetching error:', error);
      setError(error.message);
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <form onSubmit={handleSubmit} className={styles.form}>
        <label className={styles.label}>
          Prompt:
          <input
            type='text'
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className={styles.input}
          />
        </label>
        <label className={styles.label}>
          Negative Prompt:
          <input
            type='text'
            value={negativePrompt}
            onChange={(e) => setNegativePrompt(e.target.value)}
            className={styles.input}
          />
        </label>
        <div className={styles.inputGroup}>
          <label className={styles.label}>
            Width:
            <input
              type='number'
              value={width}
              onChange={(e) => setWidth(parseInt(e.target.value))}
              className={styles.input}
            />
          </label>
          <label className={styles.label}>
            Height:
            <input
              type='number'
              value={height}
              onChange={(e) => setHeight(parseInt(e.target.value))}
              className={styles.input}
            />
          </label>
        </div>
        <label className={styles.label}>
          Guidance Scale:
          <input
            type='number'
            value={guidanceScale}
            onChange={(e) => setGuidanceScale(parseInt(e.target.value))}
            className={styles.input}
          />
        </label>
        <label className={styles.label}>
          Number of Inference Steps:
          <input
            type='number'
            value={numInferenceSteps}
            onChange={(e) => setNumInferenceSteps(parseInt(e.target.value))}
            className={styles.input}
          />
        </label>
        <label className={styles.label}>
          Seed:
          <input
            type='number'
            value={seed}
            onChange={(e) => setSeed(parseInt(e.target.value))}
            className={styles.input}
          />
        </label>
        <button type='submit' className={styles.button} disabled={isLoading}>
          {isLoading ? 'Processing...' : 'Submit'}
        </button>
        {error && <p className={styles.error}>{error}</p>}
        <img src={generatedImageBase64} alt='Generated' className={styles.image} />
      </form>
    </div>
  );
}

export default PromptInput;
