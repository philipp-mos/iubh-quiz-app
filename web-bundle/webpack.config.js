const path =  require('path');
const extract = require('mini-css-extract-plugin');
const CreateFileWepack = require('create-file-webpack');
const CopyPlugin = require("copy-webpack-plugin");

const destinationDirectory = '../web-app/src/static/bundle';

module.exports = {
    mode: 'development',
    devtool: 'source-map',
    entry: {
        base: './src/modules/base/scripts/scripts.js',
        auth: './src/modules/auth/scripts/scripts.js',
        legal: './src/modules/legal/scripts/scripts.js',
        suggestquestion: './src/modules/suggestquestion/scripts/scripts.js',
        quiz: './src/modules/quiz/scripts/scripts.js',
        quizresult: './src/modules/quizresult/scripts/scripts.js'
    },
    output: {
        path: path.resolve(__dirname, destinationDirectory),
        filename: '[name].bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test:/\.(sa|sc|c)ss$/,
                use: [
                    {
                        loader: extract.loader
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            implementation: require('sass')
                        }
                    }
                ]
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            outputPath: 'images'
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new extract({
            filename: '[name].bundle.css'
        }),
        new CreateFileWepack({
            path: destinationDirectory,
            fileName: 'bundle-version.txt',
            content: Math.random().toString(36).replace(/[^a-z]+/g, '')
        }),
        new CopyPlugin({
            patterns: [
              { from: "./src/assets", to: "assets" }
            ]
        })
    ]
}