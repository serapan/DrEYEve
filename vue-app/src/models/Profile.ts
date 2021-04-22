export default class Profile {
    public total?: number;
    public normal: number = 0;
    public slightly_aggressive: number = 0;
    public fairly_aggressive: number = 0;
    public highly_aggressive: number = 0;
    public extremely_aggressive: number = 0;
    public constructor(options: any = null) {
        if (options) {
            this.total = options['TOTAL'] || 0;
            this.normal = options['NORMAL'] || 0;
            this.slightly_aggressive = options['SLIGHTLY AGGRESSIVE'] || 0;
            this.fairly_aggressive = options['FAIRLY AGGRESSIVE'] || 0;
            this.highly_aggressive = options['HIGHLY AGGRESSIVE'] || 0;
            this.extremely_aggressive = options['EXTREMELY AGGRESSIVE'] || 0;
        }
    }
}
