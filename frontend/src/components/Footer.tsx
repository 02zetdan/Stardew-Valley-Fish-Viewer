import React from 'react'

export const Footer = () => {
  return (
    <footer className="bg-dark text-white py-4 mt-auto">
      <div className="container text-center">
        <p>This site was developed by Zeth Danielsson.</p>
        <p>
          <a href="https://github.com/zethdanielsson" className="text-white" target="_blank" rel="noopener noreferrer">
            Github
          </a>
        </p>
        <p>
          <a href="https://threads.net/@zethdanielsson" className="text-white" target="_blank" rel="noopener noreferrer">
            Threads
          </a>
        </p>
        <p>
          <a href="https://www.linkedin.com/in/zethdanielsson/" className="text-white" target="_blank" rel="noopener noreferrer">
            LinkedIn
          </a>
        </p>
      </div>
    </footer>
  )
}

export default Footer;
