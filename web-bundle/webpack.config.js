const path =  require('path');
const extract = require('mini-css-extract-plugin');
const CreateFileWepack = require('create-file-webpack');

module.exports = {
    mode: 'development',
    entry: {
        base: './src/base/scripts/scripts.js',
        home: './src/home/scripts/scripts.js'
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
        })
    ]
}