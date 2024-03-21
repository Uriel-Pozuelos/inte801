/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./templates/**/*.html', './static/src/**/*.js'],
	theme: {
		extend: {}
	},
	plugins: [require('daisyui')],
	daisyui: {
		themes: [
			{
				cookies: {
					primary: '#4586FF',
					secondary: '#6F3AC5',
					accent: '#B392E8',
					neutral: '#FFE4E4',
					'base-100': '#1C020C',
					background: '#FFE4E4'
				}
			}
		]
	}
};
