var path = require('path');
// const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
        mode: 'development',
        context: path.resolve(__dirname, '../../chucksite/js'),
        entry: {
            app: './index.js',
            quill: './common/rumpus-quill.js'
        },
        devtool: 'source-map',
        cache: true,
        output: {
            path: path.resolve(__dirname, '../../chucksite/static/chucksite/js'),
            filename: '[name].bundle.js'
        },
        resolve: {
            alias: {
                'Parchment': path.resolve(__dirname, '../../node_modules/parchment/src/parchment.ts'),
                'quill$': path.resolve(__dirname, '../../node_modules/quill/quill.js'),
            },
            extensions: ['.mjs', '.js', '.ts', '.svg']
        },
        module: {
            rules: [
                {
                    test: path.join(path.resolve(__dirname, '../../'), '.') && /\.js$/,
                    exclude: /(node_modules)/,
                    use: [{
                        loader: 'babel-loader',
                        options: {
                            presets: ["@babel/preset-env", "@babel/preset-react"]
                        }
                    }]
                }, {
                    test: path.join(path.resolve(__dirname, '../../'), '.') && /\.(tsx|ts)$/,
                    loader: 'babel-loader'
                }, {
                    test: path.join(path.resolve(__dirname, '../../'), '.') && /\.svg$/,
                    use: [{
                        loader: 'html-loader',
                        options: {
                            minimize: true
                        }
                    }]
                }, {
                    test: path.join(path.resolve(__dirname, '../../'), '.') && /\.mjs$/,
                    include: /(node_modules)/,
                    type: 'javascript/auto'
                }, {
                    test: path.join(path.resolve(__dirname, '../../'), '.') && /\.css$/i,
                    use: ["style-loader", "css-loader"],
                },
            ]
        }
    }