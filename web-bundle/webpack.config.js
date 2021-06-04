const path =  require('path');
const extract = require('mini-css-extract-plugin');
const CreateFileWepack = require('create-file-webpack');
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
    mode: 'development',
    entry: {
        base: './src/modules/base/scripts/scripts.js',
        auth: './src/modules/auth/scripts/scripts.js',
        legal: './src/modules/legal/scripts/scripts.js',
        home: './src/modules/home/scripts/scripts.js'
    },
    output: {
        path: path.resolve(__dirname, '../web-app/src/static'),
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
            path: '../web-app/src/static',
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