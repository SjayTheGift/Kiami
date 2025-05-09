const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');


module.exports = {
    entry: {
        alpine: './src/js/app.js',       // Entry point for Alpine.js
    },
    output: {
        path: path.resolve(__dirname, 'static'), // Output directory
        filename: 'bundle.js', // This will output JS files named after the entry points
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader, // Extracts CSS into separate files
                    'css-loader',                 // Turns CSS into CommonJS
                    'postcss-loader',             // Processes CSS with PostCSS
                ],
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'output.css', // Output CSS file for Tailwind
        }),
    ],
    mode: 'development', // Change to 'production' for production builds
};