() => {
	const isoDates = document.getElementsByClassName('js-date-format');
	let initialDates = [];
	const startDate = new Date();

	const MS_PER_SECOND = 1000;
	const SECONDS_PER_MINUTE = 60;
	const SECONDS_PER_HOUR = 3600;

	for (const isoDate of isoDates) {
		initialDates.push(isoDate.innerText);
	}

	setInterval(() => {
		const now = new Date();

		for (let i = 0; i < isoDates.length; i++) {
			const date = initialDates[i];
			const endDate = new Date(date);
			let diffTimeInSeconds = getDiffTimeInSeconds(endDate, now);

			isoDates[i].innerHTML = replaceDateFormatJS(i, diffTimeInSeconds);
		}
	}, 1000);

	function getDiffTimeInSeconds(endDate, now) {
		const diffTimeInMSeconds = Math.abs(endDate - now);
		let diffTimeInSeconds = diffTimeInMSeconds / MS_PER_SECOND;
		diffTimeInSeconds = Math.floor(diffTimeInSeconds);

		return diffTimeInSeconds;
	}

	function getSecondsInMinutes(diffTimeInMSeconds) {
		return Math.floor(diffTimeInMSeconds / SECONDS_PER_MINUTE);
	}

	function getSecondsInHours(diffTimeInSeconds) {
		return Math.floor(diffTimeInSeconds / SECONDS_PER_HOUR);
	}

	function replaceDateFormatJS(x, diffTimeInSeconds) {
		let text = isoDates[x].innerText;

		if (diffTimeInSeconds < 2) {
			text = diffTimeInSeconds + ' second ago';
		} else if (diffTimeInSeconds < 60) {
			text = diffTimeInSeconds + ' seconds ago';
		} else if (diffTimeInSeconds < 120) {
			text = getSecondsInMinutes(diffTimeInSeconds) + ' minute ago';
		} else if (diffTimeInSeconds < 3600) {
			text = getSecondsInMinutes(diffTimeInSeconds) + ' minutes ago';
		} else if (diffTimeInSeconds < 7200) {
			text = getSecondsInHours(diffTimeInSeconds) + ' hour ago';
		} else if (diffTimeInSeconds < 86400) {
			text = getSecondsInHours(diffTimeInSeconds) + ' hours ago';
		} else {
			text = startDate.toISOString();
		}

		return text;
	}
};
