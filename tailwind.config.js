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

				cookies: {
					primary: '#7768bb',
					primaryh: '#FF9966',
					secondary: '#66CCCC',
					accent: '#da8efa',
					neutral: '#FFE4E4',
					'base-100': '#F5F5F5',
					background: '#F5F5F5',
					info: '#3399FF',
					success: '#F78DB1',
					warning: '#515d8c',
					error: '#E14E64'
				}
			}
		]
	}
};
