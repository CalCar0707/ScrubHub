import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import EmailForm from './EmailForm'; // Email Test #1

export type AppProps = {
	initialCount: number,
	someString?: string,
};
export function App({ initialCount = 0, someString }: AppProps) {
	const [count, setCount] = useState(initialCount)

	return <>
		<div>
			<a href="https://vitejs.dev" target="_blank">
				<img src={viteLogo} className="logo" alt="Vite logo" />
			</a>
			<a href="https://react.dev" target="_blank">
				<img src={reactLogo} className="logo react" alt="React logo" />
			</a>
		</div>
		<h1>Vite + React</h1>
		<div className="card">
			<button onClick={() => setCount((count) => count + 1)}>
				count is {count}
			</button>
			<p>Strings are escaped in the script tag, so they parse correctly: {someString}</p>
			<p>
				Edit <code>src/App.tsx</code> and save to test HMR
			</p>
		</div>
		<p className="read-the-docs">
			Click on the Vite and React logos to learn more
		</p>
		<EmailForm />
	</>
}

export default App
