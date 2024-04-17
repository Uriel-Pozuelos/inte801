/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./templates/**/*.html', './static/src/**/*.js'],
	theme: {
		extend: {}
	},
	plugins: [require('daisyui')],

	daisyui: {
		themes: [
			'retro',
			'dracula',
			'corporate',
			{
				// 1
				// cookies: {
				// 	primary: '#6F3AC5',
				// 	primaryh: '#B392E8',
				// 	secondary: '#B1D4FF',
				// 	accent: '#4586FF',
				// 	neutral: '#FFE4E4',
				// 	'base-100': '#1C020C',
				// 	background: '#FFE4E4'
				// }

				// cookies: {
				// 	primary: '#7768bb',
				// 	primaryh: '#FF9966',
				// 	secondary: '#66CCCC',
				// 	accent: '#66CCCC',
				// 	neutral: '#FFE4E4',
				// 	'base-100': '#FFE4E4',
				// 	background: '#f5f5f5',
				// 	info: '#39AE83',
				// 	success: '',
				// 	warning: '',
				// 	error: ''
				// }

				// chat 1
				// cookies: {
				// 	primary: '#FFB6C1',
				// 	secondary: '#FFE4E1',
				// 	accent: '#FFA07A',
				// 	neutral: '#F5F5F5',
				// 	'base-100': '#F5F5F5',
				// 	background: '#F5F5F5',
				// 	info: '#ADD8E6',
				// 	success: '#90EE90',
				// 	warning: '#FFD700',
				// 	error: '#FF6347'
				// }

				// chat 2
				cookies: {
					primary: '#FF69B4',
					secondary: '#FFC0CB',
					accent: '#FF6347',
					neutral: '#F0F8FF',
					'base-100': '#F0F8FF',
					background: '#F5F5F5',
					info: '#00BFFF',
					success: '#00FF00',
					warning: '#FFD700',
					error: '#DC143C'
				}
			}
		]
	}
};
