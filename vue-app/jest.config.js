module.exports = {
    preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
    moduleNameMapper: {
        '^@/(.*)': '<rootDir>/src/$1'
    },
    collectCoverage: false,
    coverageDirectory: '<rootDir>/tests/unit/coverage'
};
