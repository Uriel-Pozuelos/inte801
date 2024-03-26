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
					primary: '#6F3AC5',
					primaryh: '#B392E8',
					secondary: '#B1D4FF',
					accent: '#4586FF',
					neutral: '#FFE4E4',
					'base-100': '#1C020C',
					background: '#FFE4E4'
				}
			}
		]
	}
};
